# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:09:51 2020

@author: Dell
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import json

## score under 150 is blur
## 模糊检测（根据拉普拉斯变换后高低频分量）
def blur_detect(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    score = cv2.Laplacian(gray_image,cv2.CV_64F,ksize=3).var()
    return score
    
            
def reflect(img):
    mask=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('mask',mask)
    cv2.waitKey()
    cv2.destroyAllWindows()
    mask[mask>200]=255
    mask[mask<=200]=0
    
    #mask=np.zeros([147,186],np.uint8)
    #mask[30:100,70:110]=255
    #print(mask)
    
    cv2.imshow('mask',mask)
    cv2.waitKey()
    cv2.destroyAllWindows()
    kernel=np.ones((5,5),np.uint8)
    mask=cv2.dilate(mask,kernel)
    cv2.imshow('mask',mask)
    cv2.waitKey()
    cv2.destroyAllWindows()
    #dst=np.zeros([147,186])
    #dst=cv2.illuminationChange(img,mask,alpha=0.2,beta=0.4)
    dst=cv2.inpaint(img,mask,20,cv2.INPAINT_NS)
    #效果很不错，比illumination好
    return dst

def binary_threshold(image):
    _, r_th2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return r_th2

def closed_opening_operation(image): #腐蚀与膨胀（作为寻找轮廓前的步骤）
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10, 10))
    print(kernel)
    closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(15, 15))
    opening = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)

    return opening

def find_biggest_contour(image):
    # copy
    image = image.copy()
    # find each contours
    _, contours, hierarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # find the largest contour
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    biggest_contour = max(contour_sizes, key = lambda x: x[0])[1]
    mask = np.zeros(image.shape, np.uint8)
     # remove logo
    mask[0: 20, 10: 200] = 0
    cv2.drawContours(mask, [biggest_contour], -1, 255, -1) #修改过(赋不赋值都会变)

    return biggest_contour, mask

def edge(image,contour):
    edge=cv2.Canny(contour,0,255)        
    combine=np.where(edge==255) # top_left + bottom_right
    y=combine[0]
    y_min=np.min(y)
    y_max=np.max(y)
    x=combine[1]
    x_min=np.min(x)
    x_max=np.max(x)
    if y_min<20:
        y_min=20
    clipped_image = np.array(image[y_min: y_max, x_min: x_max])

    return edge,clipped_image


def clip(image): #input: cv2 image
    if image.shape==(224,224):
        print(1)
        return image
    else:
        b, g, r = cv2.split(image)
        
        binary_threshold_image = binary_threshold(r)
        
        closed_opening_image = closed_opening_operation(binary_threshold_image)
        big_contour, red_mask = find_biggest_contour(closed_opening_image)
        red_mask_border=cv2.copyMakeBorder(red_mask,1,1,1,1,cv2.BORDER_CONSTANT,value=0)
        binary_edge,clipped_image = edge(image, red_mask_border)
        height=clipped_image.shape[0]
        width=clipped_image.shape[1]
        if height<224 or width<224:
            print(2)
            return clipped_image
        else:
            resize_image = cv2.resize(clipped_image, (224, 224), interpolation=cv2.INTER_LANCZOS4) 
            print(clipped_image.shape)      
            print(3)   
            return resize_image

def closed_opening_operation_detect(image): #腐蚀与膨胀（作为寻找轮廓前的步骤）
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
    closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
    opening = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)

    return opening

def detect(image): #cv2
    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    _,ret=cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY) #阈值还可以再改
    closed_opening_image = closed_opening_operation_detect(ret) #效果：把非联通的断开，联通的合并
    edge=cv2.Canny(closed_opening_image,0,255)
    COLORS=[60,122,50]
    edge_m=np.zeros_like(image) #3通道
    cord=np.where(edge==255)
    edge_m[cord]=COLORS
    new=edge_m+image
    print('new',new)
    image = np.float32(image) / 255.0
    gx = cv2.Sobel(image,cv2.CV_32F,1,0,3)
    gy = cv2.Sobel(image,cv2.CV_32F,0,1,3)
    mag, angle = cv2.cartToPolar(gx, gy)
    

    mag[:,:,0]=np.where(mag[:,:,0]>0.15,1.0,0)

    closed_opening_image = np.float32(closed_opening_image) / 255.0
    newdot=cv2.bitwise_and(mag[:,:,0],closed_opening_image)

    COLORS=[0,0.7,0]
    dot=np.zeros_like(image) #3通道
    cord=np.where(newdot==1.0)
    dot[cord]=COLORS
    
    dot=np.uint8(dot*255)
    d=str(dot.tolist())
    with open('2.txt','w') as f:
        f.write(d)
    
    #new=np.float32(new) / 255.0
    new2=dot+new
    new2=np.uint8(new2)
    
    return new2
    
    
