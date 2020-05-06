import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.datasets
import torchvision.models as models
import torch.nn as nn
import torch.optim as optim
import time

from tensorboardX import SummaryWriter
writer=SummaryWriter('/home/are/data_cervical/pytorch_running/difmodel/SGDrun')

transform = transforms.Compose(
    [transforms.Resize((224,224)),transforms.ToTensor(),
     transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])
train_dataset=torchvision.datasets.ImageFolder('/home/are/data_cervical/pytorch_running/3_data/caijian2/train/',transform)
valid_dataset=torchvision.datasets.ImageFolder('/home/are/data_cervical/pytorch_running/3_data/caijian2/valid/',transform)

train_loader=torch.utils.data.DataLoader(train_dataset,batch_size=32,shuffle=True,num_workers=5)
valid_loader=torch.utils.data.DataLoader(valid_dataset,batch_size=32,shuffle=True,num_workers=5)
print('data load successfully')


#model_ft=models.AlexNet(num_classes=3)
#model_ft=models.vgg16(pretrained=False,num_classes=3)
model_ft=models.resnet50(pretrained=True)
num_ftrs=model_ft.fc.in_features
model_ft.fc=nn.Linear(num_ftrs,3) 
#model_ft.load_state_dict(torch.load('/home/are/data_cervical/pytorch_running/third/resnet50/Adam/resnet50_weight.pth'))
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model_ft=model_ft.to(device)
print(model_ft)
#num_parameters = sum([param.nelement() for param in model_ft.parameters()])
#with open('resnet50.txt', "a+") as fp:    
 #   fp.write("Number of parameters: \n"+str(num_parameters)+"\n")

learning_rate=0.001
criterion=nn.CrossEntropyLoss()
optimizer=optim.SGD(model_ft.parameters(),lr=0.001,momentum=0.9)

dataloader={'train':train_loader,'valid':valid_loader}
dataset={'train':train_dataset,'valid':valid_dataset}

best_acc=0
num_epochs=150
for epoch in range(num_epochs):
    since=time.time()
    print('epoch:',epoch)
    print('-'*10)
        
    for phase in ['train','valid']:            
        if phase=='train':
            model_ft.train(True)
        else:
            model_ft.train(False)
        running_loss=0.0
        running_corrects=0        
        for i, data in enumerate(dataloader[phase], 0):
            inputs, labels = data
            inputs=torch.autograd.Variable(inputs.to(device))  #数据和标签要放到GPU上
            labels=torch.autograd.Variable(labels.to(device))        
            optimizer.zero_grad()
                # forward + backward + optimize
            outputs = model_ft(inputs)
            loss = criterion(outputs, labels)
            _,preds=torch.max(outputs.data,1)
            if phase=='train':
                loss.backward()
                optimizer.step()
            running_loss+=loss.item()
            running_corrects+=(torch.sum(preds==labels.data)).item()
        print(running_loss)
        print(running_corrects)       
        print(len(dataset[phase]))
        epoch_loss=running_loss/len(dataset[phase])
        epoch_acc=running_corrects/len(dataset[phase])
        
        if phase=='train':
            writer.add_scalars('loss_train_val',{'train':epoch_loss},epoch)
            writer.add_scalars('acc_train_val',{'train':epoch_acc},epoch)
        else:
            
            writer.add_scalars('loss_train_val',{'valid':epoch_loss},epoch)
            writer.add_scalars('acc_train_val',{'valid':epoch_acc},epoch)
        
        print('{} loss: {:.8f} acc:{:.8f}'.format(phase,epoch_loss,epoch_acc))
        if phase=='valid' and epoch_acc>best_acc:
           
            best_acc=epoch_acc
            best_model_wts=model_ft.state_dict()
            torch.save(best_model_wts,'best_SGD_weight.pth')   
    time_elapsed= time.time()-since
    
    print('training time:',time_elapsed)
