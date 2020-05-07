import os
import argparse
import shutil
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
from torchvision import datasets, transforms
from torch.autograd import Variable
import preresnet
import time
from tensorboardX import SummaryWriter
writer=SummaryWriter('/home/are/data_cervical/pytorch_running/third/slim_zye/run90')
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

parser = argparse.ArgumentParser(description='PyTorch Slimming CIFAR training')
parser.add_argument('--sparsity-regularization', '-sr', dest='sr', action='store_true',
                    help='train with channel sparsity regularization')
parser.add_argument('--s', type=float, default=0.0001,
                    help='scale sparse rate (default: 0.0001)')
parser.add_argument('--refine', default='', type=str, metavar='PATH',
                    help='path to the pruned model to be fine tuned')
                    
parser.add_argument('--epochs', type=int, default=160, metavar='N',
                    help='number of epochs to train (default: 160)')                    
parser.add_argument('--save', default='./logs', type=str, metavar='PATH',
                    help='path to save prune model (default: current directory)')
                   
args = parser.parse_args()

save=args.save
if not os.path.exists(save):
    os.makedirs(save)

transform = transforms.Compose(
    [transforms.Resize((224,224)),transforms.ToTensor(),
     transforms.Normalize((0.5941, 0.3818, 0.3370), (0.1508 ,0.1404, 0.1222))])
train_dataset=torchvision.datasets.ImageFolder('/home/are/data_cervical/pytorch_running/3_data/caijian2/train/',transform)
valid_dataset=torchvision.datasets.ImageFolder('/home/are/data_cervical/pytorch_running/3_data/caijian2/valid/',transform)
train_loader=torch.utils.data.DataLoader(train_dataset,batch_size=32,shuffle=True,num_workers=4)
valid_loader=torch.utils.data.DataLoader(valid_dataset,batch_size=32,shuffle=True,num_workers=4)                  

if args.refine:
    save=args.refine
    checkpoint = torch.load(os.path.join(args.refine,'pruned.pth'))
    model = preresnet.ResNet(cfg=checkpoint['cfg'])
    model.load_state_dict(checkpoint['state_dict'])
    
else:
    model = preresnet.ResNet()

#cfg=[32, 64, 28, 125, 125, 64, 11, 125, 64, 8, 125, 128, 28, 169, 169, 128, 39, 169, 128, 27, 169, 128, 25, 169, 256, 51, 224, 224, 256, 49, 224, 256, 33, 224, 256, 31, 224, 256, 37, 224, 256, 37, 224, 512, 64, 430, 430, 512, 70, 430, 75, 58, 430]
#model = preresnet.ResNet(cfg=cfg)  
 
model=model.to(device)
num_parameters = sum([param.nelement() for param in model.parameters()])
savepath = os.path.join(save, "pruned.txt")

with open(savepath, "a+") as fp:    
    fp.write("Number of parameters: \n"+str(num_parameters)+"\n")
    
 
#model.load_state_dict(torch.load('/home/are/data_cervical/pytorch_running/third/resnet50/Adam/resnet50_weight.pth'))
criterion=nn.CrossEntropyLoss()
optimizer=torch.optim.Adam(model.parameters(),weight_decay=1e-4,lr=0.001,betas=(0.9,0.99))

def updateBN():
    for m in model.modules():
        if isinstance(m, nn.BatchNorm2d):
            m.weight.grad.data.add_(args.s*torch.sign(m.weight.data))  # L1

def train(epoch):
    model.train(True)
    running_loss=0
    running_corrects=0
    since=time.time()
    for batch_idx, (inputs, labels) in enumerate(train_loader,0):
        inputs=torch.autograd.Variable(inputs.to(device))  #数据和标签要放到GPU上
        labels=torch.autograd.Variable(labels.to(device))
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        _,preds=torch.max(outputs.data,1)
        loss.backward()
        if args.sr:
            updateBN()
        optimizer.step()
        running_loss+=loss.item()
        running_corrects+=(torch.sum(preds==labels.data)).item()
        if batch_idx % 100 == 0:
            print('Train Epoch: {} [{}/{} ({:.1f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(inputs), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))
    
    epoch_loss=running_loss/len(train_dataset)
    epoch_acc=running_corrects/len(train_dataset)
    writer.add_scalars('loss_train_val',{'train':epoch_loss},epoch)
    writer.add_scalars('acc_train_val',{'train':epoch_acc},epoch)
    time_elapsed= time.time()-since
    print('epoch_loss',epoch_loss)
    print('epoch_acc',epoch_acc)
    print('time:',time_elapsed)
    return
        
def test():
    model.eval()
    test_loss = 0
    running_corrects = 0
    for batch_idx, (inputs, labels) in enumerate(valid_loader,0):
        inputs=torch.autograd.Variable(inputs.to(device))  #数据和标签要放到GPU上
        labels=torch.autograd.Variable(labels.to(device))
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        _,preds=torch.max(outputs.data,1)
        running_corrects+=(torch.sum(preds==labels.data)).item()
        
        test_loss+=loss.item()
    test_loss /= len(valid_dataset)
    
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.1f}%)\n'.format(
        test_loss, running_corrects, len(valid_dataset),
        100. * running_corrects / len(valid_dataset)))
    return test_loss, running_corrects / float(len(valid_dataset))
    

best_prec = 0

for epoch in range(0,args.epochs):
    train(epoch)
    loss,prec=test()
    writer.add_scalars('loss_train_val',{'valid':loss},epoch)
    writer.add_scalars('acc_train_val',{'valid':prec},epoch)
    if prec>best_prec:
        best_prec=prec
        torch.save(model.state_dict(),os.path.join(args.save,'finetune.pth'))

