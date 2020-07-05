#!/usr/bin/python
#--coding:utf8--
import numpy as np
import cv2
import tkinter as tk  
from tkinter import *
import tkinter.ttk
from tkinter.ttk import Frame
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import datetime
import os
import time
import preresnet
#from classification import model_predict
from preprocess import blur_detect
from preprocess import clip
from preprocess import detect

white       = "#ffffff"
lightBlue2  = "#adc5ed"
font        = "Constantia"
fontButtons = (font, 14)
maxWidth    = 1200
maxHeight   = 680
flag        = 1 #used to judge whether to imshow the video or just a picture
capture=cv2.VideoCapture(0)


from PIL import Image
import torchvision.transforms as transforms
import torch
PATH='/home/are/code/pruned_whole.pth' # load in advance, save time
net=torch.load(PATH,map_location='cpu')
print(net)
net.eval()
def model_predict(img):
	print('1')
	simple_transform=transforms.Compose([transforms.Resize((224,224)),transforms.ToTensor(),transforms.Normalize([0.5941,0.3818,0.3370],[0.1508,0.1404,0.1222])])	
	input=simple_transform(img)	
	print('2')
	input=torch.unsqueeze(input,0)	
	output=net(input)
	print('3')
	print('output',output)
	_,preds=torch.max(output.data,1)

	return preds.item()	

def cameravideo():
	#global mainFrame
	#global display_window_video
	global display_window_img  
	#global flag
	#print('enter')
	global startButton
	#startButton = Button(mainWindow,text="check_frame",font=fontButtons,width=15,height=1,command=lambda:check_frame_button())
	startButton.place(x=maxWidth*0.62,y=maxHeight*0.15)    
	alltext = 'capture image'
	receive_from_detect.config(text=alltext)
       
def show_frame():
	global display_window_video
	
	#print('frame')	
	ret, frame = capture.read()
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	img   = Image.fromarray(cv2image)
	imgtk = ImageTk.PhotoImage(image = img)
	display_window_video.imgtk = imgtk
	display_window_video.configure(image=imgtk)
	display_window_video.after(10, show_frame)
		
def recollect():
	display_window_img.grid_forget()
	display_window_video.grid(row=0, column=0)
	alltext = 'capture image'
	receive_from_detect.config(text=alltext)
	clip_frameButton.place_forget()
	predict_frameButton.place_forget()



    
    
def check_frame_button():
	global flag
	global display_window_video
	global display_window_img
	global mainFrame
	global recollectButton
	global clip_frameButton

	#flag=0
	#print(display_window.grid_slaves(0,0))

	display_window_video.grid_forget()
	#print('check')	
	display_window_img.grid(row=0, column=0)	
	ret, frame = capture.read()
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	img   = Image.fromarray(cv2image)
	imgtk = ImageTk.PhotoImage(image=img)
	display_window_img.imgtk = imgtk
	display_window_img.configure(image=imgtk)
	alltext = 'image quality detection......'
	receive_from_detect.config(text=alltext)
	detection_score=blur_detect(frame)
	print(detection_score)
	if detection_score<40:
		alltext = "Image blur,please recollect"
		receive_from_detect.config(text=alltext,fg="red")
		#recollectButton=Button(mainWindow,text="collect again",font=fontButtons,width=15,height=1,command=recollect)
		recollectButton.place(x=maxWidth*0.62,y=maxHeight*0.25)
	else:
		alltext = 'quality test pass and waiting......'
		receive_from_detect.config(text=alltext,fg="green")
		clip_frameButton=Button(mainWindow,text="clip",font=fontButtons,width=15,height=1,command=lambda:clipframe(cv2image))
		clip_frameButton.place(x=maxWidth*0.62,y=maxHeight*0.35)
		



		

		
def choosefile():
	global display_window_video
	global display_window_img
	global mainFrame
	global Check_Button_right
	global img_open
	file_path = askopenfilename()
	img_open = Image.open(file_path)
	img_resize = img_open.resize((624,416))
	display_window_video.grid_forget()
	#display_window_img = tk.Label(mainFrame)
	display_window_img.grid(row=0, column=0)
	imgtk = ImageTk.PhotoImage(image=img_resize)
	display_window_img.imgtk = imgtk
	display_window_img.configure(image=imgtk)

	Check_Button_right = Button(mainWindow,text="check_image",font=fontButtons,width=15,height=1,command=lambda:check_img_button(img_open))
	Check_Button_right.place(x=maxWidth*0.82,y=maxHeight*0.15) 
	
def check_img_button(img):
	
	global clip_imgButton
	alltext = 'image quality detection......'
	receive_from_detect.config(text=alltext)
	img=cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)  #because in preprocess.py the img must be cv2
	detection_score=blur_detect(img)
	if detection_score<150:  #the score is not definitd
		alltext = ""
		receive_from_detect.config(text=alltext,fg="red")
	else:
		alltext = 'quality test pass and waiting......'
		receive_from_detect.config(text=alltext,fg="green")
		clip_imgButton=Button(mainWindow,text="clip",font=fontButtons,width=15,height=1,command=lambda:clipimg(img))
		clip_imgButton.place(x=maxWidth*0.82,y=maxHeight*0.25)
		
		
		
def clipimg(img):
	global display_window_img
	global predict_imgButton
	global img_resize_cv2
	print(img)
	clip_img=clip(img) #
	print('clip',clip_img.shape)
	img_resize_cv2 = cv2.resize(clip_img,(448,448))
	img_resize = cv2.cvtColor(img_resize_cv2, cv2.COLOR_BGR2RGB) # cv2 => image
	imgtk = ImageTk.PhotoImage(image=Image.fromarray(img_resize))
	display_window_img.imgtk = imgtk
	display_window_img.configure(image=imgtk)
	cv2image = cv2.cvtColor(clip_img, cv2.COLOR_BGR2RGB) #
	predict_imgButton=Button(mainWindow,text="predict",font=fontButtons,width=15,height=1,command=lambda:predict_img(img_open))
	predict_imgButton.place(x=maxWidth*0.82,y=maxHeight*0.35)
	
def clipframe(img):
	global display_window_img
	global predict_frameButton
	print(img)
	clip_img=clip(img) #
	print('clip',clip_img.shape)
	img_resize = cv2.resize(clip_img,(448,448))
	print('resize',img_resize)
	#img_resize = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB) # cv2 => image
	imgtk = ImageTk.PhotoImage(image=Image.fromarray(img_resize))
	display_window_img.imgtk = imgtk
	display_window_img.configure(image=imgtk)
	#cv2image = cv2.cvtColor(clip_img, cv2.COLOR_BGR2RGB) #
	recollectButton.place(x=maxWidth*0.62,y=maxHeight*0.25)
	predict_frameButton=Button(mainWindow,text="predict",font=fontButtons,width=15,height=1,command=lambda:predict_frame(clip_img))
	predict_frameButton.place(x=maxWidth*0.62,y=maxHeight*0.45)


def predict_img(img):  #input :cv2 img

	global predict_result
	
	
	#result=model_predict(Image.fromarray(img.astype('uint8'))) 
	#result=model_predict(Image.fromarray(img)) 
	result=model_predict(img)
	print('result',result)
	print(type(result))
	if result==0:
		pred_chinese = "正常或炎症或宫颈息肉"
		print('enter')
	if result==2:
		pred_chinese = "低SIL" #pay attention to this
	if result==1:
		pred_chinese = "高SIL及以上"
		print('high')
		detect_Button=Button(mainWindow,text="detect",font=fontButtons,width=15,height=1,command=lambda:detect_img(img_resize_cv2))
		detect_Button.place(x=maxWidth*0.82,y=maxHeight*0.55)
	predict_result.config(text='result:'+pred_chinese)

def detect_img(img): # cv2
	img_with_detect=detect(img)
	#img_with_detect = Image.open('home/are/code/detect.jpg')
	img_with_detect = cv2.cvtColor(img_with_detect, cv2.COLOR_BGR2RGB)
	print(img_with_detect)
	print(type(img_with_detect))
	#imgtk = ImageTk.PhotoImage(image=Image.fromarray(np.uint8(img_with_detect*255)))
	imgtk = ImageTk.PhotoImage(image=Image.fromarray(img_with_detect))
	display_window_img.imgtk = imgtk
	display_window_img.configure(image=imgtk)

def predict_frame(img):  #input :cv2 img

	global predict_result
	
	
	#result=model_predict(Image.fromarray(img.astype('uint8'))) 
	result=model_predict(Image.fromarray(img)) 
	#result=model_predict(img)
	print('result',result)
	print(type(result))
	if result==0:
		pred_chinese = "正常或炎症或宫颈息肉"
		print('enter')
	if result==2:
		pred_chinese = "低SIL" #pay attention to this
	if result==1:
		pred_chinese = "高SIL及以上"
		print('high')
	predict_result.config(text='result:'+pred_chinese)


def rechoose():
	
	display_window_img.grid_forget()
	display_window_video.grid(row=0, column=0)
	alltext='choose mode'
	receive_from_detect.config(text=alltext,fg='black') 
	pred_chinese='result:'
	predict_result.config(text='result:')
	if var.get()==1:

		startButton.place_forget()  
		recollectButton.place_forget()
		clip_frameButton.place_forget()
		predict_frameButton.place_forget()
	else:

		Check_Button_right.place_forget()
		clip_imgButton.place_forget()
		predict_imgButton.place_forget()


	
alltext='choose mode'
pred_chinese='result:'
mainWindow = tk.Tk()
mainWindow.title('cervical cancer')

screenWidth = mainWindow.winfo_screenwidth()
screenHeight = mainWindow.winfo_screenheight()
print(screenHeight)
print(screenWidth)
mainWindow.configure(bg=lightBlue2)
mainWindow.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,(screenWidth-maxWidth)/2,(screenHeight-maxHeight)/2))
mainWindow.resizable((screenWidth-maxWidth)/2,(screenHeight-maxHeight)/2)

closeButton = Button(mainWindow,text="close",font=fontButtons,width=5,height=1,command=lambda: mainWindow.destroy())
#closeButton.configure(command=lambda: mainWindow.destroy())              
closeButton.place(x=maxWidth*0.03,y=maxHeight*0.89)

receive_from_detect = Label(mainWindow,text=alltext,font=fontButtons,width=50,height=2)
receive_from_detect.place(x=maxWidth*0.15,y=maxHeight*0.82)
mainFrame=Frame(mainWindow)
mainFrame.place(x=maxWidth*0.045, y=maxHeight*0.035) 
display_window_img = tk.Label(mainFrame)
display_window_video = tk.Label(mainFrame)
display_window_video.grid(row=0, column=0)	
show_frame()
restartButton = Button(mainWindow,text="update",font=fontButtons,width=8,height=1,command=lambda: rechoose())   
restartButton.place(x=maxWidth*0.03,y=maxHeight*0.8)

predict_result = Label(mainWindow,text=pred_chinese,font=("Constantia",16),width=30,height=2)
predict_result.place(x=maxWidth*0.65,y=maxHeight*0.82)
var = IntVar()            #用来表示按钮是否选中
check1 = Radiobutton(mainWindow,text='camera mode',font=fontButtons,variable=var,value=1,width=15,height=1)
check1.configure(command=cameravideo)
check2 = Radiobutton(mainWindow,text='image mode',font=fontButtons,variable=var,value=2,width=15,height=1)
check2.configure(command=choosefile)
check1.place(x=maxWidth*0.62,y=maxHeight*0.05)
check2.place(x=maxWidth*0.82,y=maxHeight*0.05)
startButton = Button(mainWindow,text="check_frame",font=fontButtons,width=15,height=1,command=lambda:check_frame_button())
recollectButton=Button(mainWindow,text="collect again",font=fontButtons,width=15,height=1,command=recollect)

#predict_frameButton=Button(mainWindow,text="predict",font=fontButtons,width=15,height=1,command=lambda:predict(frame))
print('3')
if __name__=="__main__":
    mainWindow.mainloop()  #Starts GUI
    #print(flag)
    
		
			
			
			
			
	