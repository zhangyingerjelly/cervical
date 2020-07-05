from PIL import Image
import torchvision.transforms as transforms
import torch
def model_predict(img):
	simple_transform=transforms.Compose([transforms.Resize((224,224)),transforms.ToTensor(),transforms.Normalize([0.5941,0.3818,0.3370],[0.1508,0.1404,0.1222])])	
	input=simple_transform(img)	
	input=torch.unsqueeze(input,0)	
	PATH='/home/are/pytorch/resnet50.pth'
	net=torch.load(PATH,map_location='cpu')
	net.eval()
	output=net(input)
	_,preds=torch.max(output.data,1)

	return preds.item()
