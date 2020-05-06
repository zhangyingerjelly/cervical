import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.datasets
import torchvision.models as models
import torch.nn as nn
import torch.optim as optim
import glob
import os
import numpy as np
import time

from tensorboardX import SummaryWriter
writer=SummaryWriter('/home/are/data_cervical/pytorch_running/difclass/run241')

transform = transforms.Compose(
    [transforms.Resize((224,224)),transforms.ToTensor(),
     transforms.Normalize((0.5941, 0.3818, 0.3370), (0.1508 ,0.1404, 0.1222))])
train_dataset=torchvision.datasets.ImageFolder('/home/are/data_cervical/pytorch_running/3_data/caijian2/train/',transform)
valid_dataset=torchvision.datasets.ImageFolder('/home/are/data_cervical/pytorch_running/3_data/caijian2/valid/',transform)
train_loader=torch.utils.data.DataLoader(train_dataset,batch_size=32,shuffle=True,num_workers=5)
valid_loader=torch.utils.data.DataLoader(valid_dataset,batch_size=32,shuffle=True,num_workers=5)

model_ft=models.resnet50(pretrained=True)
#print(model_ft)
num_ftrs=model_ft.fc.in_features
model_ft.fc=nn.Linear(num_ftrs,3)  
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model_ft=model_ft.to(device)

criterion=nn.CrossEntropyLoss(weight=(torch.tensor([2.0,4.0,1.0])).to(device))
#criterion=nn.CrossEntropyLoss()
optimizer=torch.optim.Adam(model_ft.parameters(),weight_decay=1e-4,lr=0.001,betas=(0.9,0.99))

save_path='/home/are/data_cervical/pytorch_running/difclass'
dataloader={'train':train_loader,'valid':valid_loader}
dataset={'train':train_dataset,'valid':valid_dataset}
num_epochs=250
best_acc=0 # (total_acc+recall_3+pre_1)/3

for epoch in range(num_epochs):
    since=time.time()
    print('epoch:',epoch)
    print('-'*10)
        
    for phase in ['train','valid']:        
        if phase=='train':
            model_ft.train(True)
        else:
            model_ft.eval()
        running_loss=0.0
        running_corrects=0
        c1=0
        c2=0
        c3=0
        n1=0
        n2=0
        n3=0
        p1=0 #记录被预测为第一类的数量，为了计算第一类的精确值
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
            
            #1
            label1=(labels.data==0)
            n1+=sum(label1.data).item()    
            pred1=(preds==0)
            c1+=torch.sum(label1*pred1).item()
            p1+=sum(pred1).item()
            
            #2
            label2=(labels.data==2)
            pred2=(preds==2)
            c2+=sum(label2*pred2).item()
            n2+=sum(label2).item()
            #3
            label3=(labels.data==1)
            pred3=(preds==1)
            c3+=sum(label3*pred3).item()
            n3+=sum(label3).item()
            

        print(running_loss)
        print('all correct:',running_corrects)       
        print('total num:',len(dataset[phase]))
        epoch_loss=running_loss/len(dataset[phase])
        epoch_acc=running_corrects/len(dataset[phase])
        
        recall_1=c1/n1
        recall_2=c2/n2
        recall_3=c3/n3
        pre_1=c1/p1
        print('class1:',c1,n1,recall_1)
        print('class2:',c2,n2,recall_2) #就真的代表第二类
        print('class3:',c3,n3,recall_3) 
        print('class1_pre:',c1,p1,pre_1)
        print('{} loss: {:.8f} acc:{:.8f}'.format(phase,epoch_loss,epoch_acc))
        if phase=='train':
            #train_loss.append(epoch_loss)
            #train_acc.append(epoch_acc)
            writer.add_scalars('loss_train_val',{'train':epoch_loss},epoch)
            writer.add_scalars('acc_train_val',{'train':epoch_acc},epoch)
            #if epoch%40==0: #每隔一段时间保存一次
             #   state={'net':model_ft.state_dict(),'optimizer':optimizer.state_dict(),'epoch':epoch}
              #  dir=os.path.join(save_path,'epoch_{}.pth'.format(epoch))
               # torch.save(state,dir)
        else:
            #valid_loss.append(epoch_loss)
            #valid_acc.append(epoch_acc)
            writer.add_scalars('loss_train_val',{'valid':epoch_loss},epoch)
            writer.add_scalars('acc_train_val',{'valid':epoch_acc},epoch)
            
            writer.add_scalars('acc_class_val',{'total':epoch_acc},epoch)
            writer.add_scalars('acc_class_val',{'class1':recall_1},epoch)
            writer.add_scalars('acc_class_val',{'class2':recall_2},epoch)
            writer.add_scalars('acc_class_val',{'class3':recall_3},epoch)
            
        compre_acc=(epoch_acc+recall_3+pre_1)/3
        print('compre_acc:',compre_acc)
        #if phase=='valid' and compre_acc>best_acc:
        if phase=='valid' and compre_acc>best_acc:
            best_total_acc=epoch_acc
            best_recall3=recall_3
            best_pre1=pre_1
            best_acc=compre_acc
            #best_acc=epoch_acc
            best_model_wts=model_ft.state_dict()
            torch.save(best_model_wts,'weight241.pth')

    time_elapsed= time.time()-since
    print('training time:',time_elapsed)

#print('best acc',best_acc,'best total:',best_total_acc,'best_recall3',best_recall3)
print('best acc',best_acc)