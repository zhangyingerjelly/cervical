import os
import argparse
import numpy as np
import torch
import torch.nn as nn
from torch.autograd import Variable
import torchvision
from torchvision import datasets, transforms
import preresnet

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
parser = argparse.ArgumentParser(description='PyTorch Slimming CIFAR prune')
parser.add_argument('--percent', type=float, default=0.5,
                    help='scale sparse rate (default: 0.5)')
parser.add_argument('--model', default='', type=str, metavar='PATH',
                    help='path to the model (default: none)')
parser.add_argument('--save', default='./logs', type=str, metavar='PATH',
                    help='path to save pruned model (default: none)')    

args = parser.parse_args()
savepath=os.path.join(args.save,'percent_{}'.format(args.percent))
if not os.path.exists(savepath):
    os.makedirs(savepath)                    
                   
model = preresnet.ResNet()
model=model.to(device)  
model.load_state_dict(torch.load(args.model))

total = 0
for m in model.modules():  #是一串不同等级的
    if isinstance(m, nn.BatchNorm2d):
        total += m.weight.data.shape[0]

bn = torch.zeros(total)
index = 0
for m in model.modules():
    if isinstance(m, nn.BatchNorm2d):
        size = m.weight.data.shape[0]
        bn[index:(index+size)] = m.weight.data.abs().clone()
        index += size
        
y, i = torch.sort(bn)
thre_index = int(total * args.percent)
thre = y[thre_index]   # thre 是第thre_index个
thre=thre.cuda()

#********************************预剪枝*********************************
pruned=0
cfg=[]

#对于batchnorm2d :running_mean和running_var不是学习到的参数，weight 和bias才是
# https://blog.csdn.net/LoseInVain/article/details/86476010

for k,m in enumerate(model.modules()):
    if isinstance(m,nn.BatchNorm2d):
        weight_copy=m.weight.data.abs().clone()
        mask=weight_copy.gt(thre).float()  #gt: 比较元素大小，大于则为1
        pruned=pruned+mask.shape[0]-torch.sum(mask)
        cfg.append(int(torch.sum(mask))) 
        
print(cfg)
# 先让没有0出现：每个数量至少是4
for i in range(len(cfg)):
    if cfg[i]==0:
        cfg[i]=4
# cfg
# [32, 64, 28, 119, 125, 64, 11, 116, 64, 8, 115, 128, 28, 166, 169, 128, 39, 150, 128, 27, 159, 128, 25, 164, 256, 51, 223, 224, 256, 49, 235, 256, 33, 234, 256, 31, 200, 256, 37, 238, 256, 37, 231, 512, 64, 1986, 2031, 512, 70, 1997, 75, 58, 430]
#特殊层，必须保持一致
join_layer=[[3,4,7,10],
[13,14,17,20,23],
[26,27,30,33,36,39,42],
[45,46,49,52]]
after=[]
for i in range(len(join_layer)):
    num=[cfg[j] for j in join_layer[i]]
    
    num=sorted(num)
    
    value=num[len(join_layer[i])//2]
    
    after+=[value]*len((join_layer[i]))

# 修正cfg
j=0
for layer in join_layer:
    for i in layer:
        
        cfg[i]=after[j]
        j+=1
print(cfg)
# cfg
#[32, 64, 28, 119, 119, 64, 11, 119, 64, 8, 119, 128, 28, 164, 164, 128, 39, 164, 128, 27, 164, 128, 25, 164, 256, 51, 231, 231, 256, 49, 231, 256, 33, 231, 256, 31, 231, 256, 37, 231, 256, 37, 231, 512, 64, 1997, 1997, 512, 70, 1997, 75, 58, 1997]
prune_percent=1-sum(cfg)/26560 #26560是原始结构中的总数
with open(os.path.join(savepath,'pruned.txt'), "a+") as fp: 
    fp.write("pruned percent: \n"+str(prune_percent)+"\n")
    fp.write("Configuration: \n"+str(cfg)+"\n")
    
cfg_mask=[] 
cfg_index=0 
for m in model.modules():
    if isinstance(m, nn.BatchNorm2d): 
        weight_copy=m.weight.data.abs().clone()
        
        y, index = torch.sort(weight_copy,descending=True) # index 代表在原来中的位置
       
        left=index[:cfg[cfg_index]]  #剩下来的通道的index
   
        cfg_index+=1
        size = m.weight.data.shape[0]
        
        mask=torch.zeros(size)
        mask[left]=1
        mask=mask.cuda()
        cfg_mask.append(mask.clone())
        m.weight.data.mul_(mask)
        m.bias.data.mul_(mask)

       
#********************************预剪枝后model测试*********************************

transform = transforms.Compose(
    [transforms.Resize((224,224)),transforms.ToTensor(),
     transforms.Normalize((0.5941, 0.3818, 0.3370), (0.1508 ,0.1404, 0.1222))])
#train_dataset=torchvision.datasets.ImageFolder('/home/are/data_cervical/pytorch_running/3_data/caijian2/train/',transform)
valid_dataset=torchvision.datasets.ImageFolder('/home/are/data_cervical/pytorch_running/3_data/caijian2/valid/',transform)
#train_loader=torch.utils.data.DataLoader(train_dataset,batch_size=32,shuffle=True,num_workers=4)
valid_loader=torch.utils.data.DataLoader(valid_dataset,batch_size=32,shuffle=True,num_workers=4)                  
criterion=nn.CrossEntropyLoss()


  
def test():
    model.eval()
    #print(model)
    test_loss = 0
    running_corrects = 0
    for batch_idx, (inputs, labels) in enumerate(valid_loader,0):
        inputs=torch.autograd.Variable(inputs.to(device))  #数据和标签要放到GPU上
        labels=torch.autograd.Variable(labels.to(device))
        
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

loss,acc=test() 
        
#********************************剪枝*********************************
# ps: 此结构中conv2d不存在bias，
#     conv2d m.weight.shape  [64,3,7,7] 进在后，出在前
newmodel = preresnet.ResNet(cfg=cfg)# 一定要写等于号！！！
newmodel=newmodel.to(device)                  
layer_id_in_cfg=0
special_id=[4,14,27,46] #出现的downsample结构会破坏conv,batch 的顺序，此时conv2d的input不是start_mask,而是再往前推4个
start_mask=torch.ones(3)# 初始input 的3通道
end_mask=cfg_mask[layer_id_in_cfg] 
for [m0,m1] in zip(model.modules(),newmodel.modules()):
    if isinstance(m0,nn.BatchNorm2d):
        idx1 = np.squeeze(np.argwhere(np.asarray(end_mask.cpu().numpy())))
        if idx1.size==1:
            idx1=np.resize(idx1,(1,))
        m1.weight.data = m0.weight.data[idx1].clone()
        m1.bias.data = m0.bias.data[idx1].clone()
        m1.running_mean = m0.running_mean[idx1].clone()
        m1.running_var = m0.running_var[idx1].clone()
        layer_id_in_cfg+=1
        if layer_id_in_cfg in special_id:
            start_mask=cfg_mask[layer_id_in_cfg-4].clone()
        else:
            start_mask = end_mask.clone()
        if layer_id_in_cfg < len(cfg_mask):  
            end_mask = cfg_mask[layer_id_in_cfg] 
        
        
    elif isinstance(m0, nn.Conv2d):
        idx0 = np.squeeze(np.argwhere(np.asarray(start_mask.cpu().numpy())))
        idx1 = np.squeeze(np.argwhere(np.asarray(end_mask.cpu().numpy())))
        if idx0.size == 1:
            idx0 = np.resize(idx0, (1,))
        if idx1.size == 1:
            idx1 = np.resize(idx1, (1,))
        w = m0.weight.data[:, idx0, :, :].clone() #torch.Size([64, 3, 7, 7]) 出在前，进在后
        m1.weight.data = w[idx1, :, :, :].clone()
    elif isinstance(m0, nn.Linear):
        idx0 = np.squeeze(np.argwhere(np.asarray(end_mask.cpu().numpy()))) #[3,2048]
        m1.weight.data = m0.weight.data[:, idx0].clone()
        m1.bias.data=m0.bias.data.clone()

'''
print('newmodel  layer1[1].bn1')
print(newmodel.layer1[1].conv3.weight.data.shape)
print(newmodel.layer1[1].conv3.weight.data)
'''
'''
def newmodelone(input):
    newmodel.eval()
    print('input',input)
    input=torch.autograd.Variable(input.to(device))  #数据和标签要放到GPU上
    #label=torch.autograd.Variable(label.to(device))
    output=newmodel(input)
    print('out',output)

newmodelone(input.unsqueeze(0))
'''

def newtest():
    newmodel.eval()
    #print(model)
    test_loss = 0
    running_corrects = 0
    for batch_idx, (inputs, labels) in enumerate(valid_loader,0):
        inputs=torch.autograd.Variable(inputs.to(device))  #数据和标签要放到GPU上
        labels=torch.autograd.Variable(labels.to(device))        
        outputs = newmodel(inputs)
        loss = criterion(outputs, labels)
        _,preds=torch.max(outputs.data,1)
        running_corrects+=(torch.sum(preds==labels.data)).item()        
        test_loss+=loss.item()
    test_loss /= len(valid_dataset)
    
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.1f}%)\n'.format(
        test_loss, running_corrects, len(valid_dataset),
        100. * running_corrects / len(valid_dataset)))
    return test_loss, running_corrects / float(len(valid_dataset))

loss,acc=newtest()
torch.save({'cfg':cfg,'state_dict':newmodel.state_dict()},os.path.join(savepath, 'pruned.pth'))