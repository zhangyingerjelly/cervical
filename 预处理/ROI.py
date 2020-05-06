# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:33:06 2019

@author: Dell
"""
'''
attention:
    opencv: b,g,r
    cv2imread() cv2.imshow 配套
    plt:r,g,b
    
'''
import cv2  #
#import matplotlib.pyplot as plt
import numpy as np
import os

def binary_threshold(image):
    _, r_th2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #最大类间方差找到阈值，会受到反射影响
    #_, r_th2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY )
    #_, r_th2 = cv2.threshold(image, 0, 180, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return r_th2

def closed_opening_operation(image): #腐蚀与膨胀（作为寻找轮廓前的步骤）
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10, 10))
    closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(15, 15))
    opening = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)

    return opening

def find_biggest_contour(image):
    # copy
    image = image.copy()

    # find each contours
    contours, hierarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # find the largest contour
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    biggest_contour = max(contour_sizes, key = lambda x: x[0])[1]

    mask = np.zeros(image.shape, np.uint8)
     # remove logo
    mask[0: 20, 10: 200] = 0
    cv2.drawContours(mask, [biggest_contour], -1, 255, -1) #修改过(赋不赋值都会变)

   

    return biggest_contour, mask

def clip_resize_operation(image, contour):
    ellipse = cv2.fitEllipse(contour)  #拟合一个椭圆使轮廓尽量在圆上
    #print('ellipse',ellipse)
    center = ellipse[0]
    size = ellipse[1]  #短轴长轴
    angle = ellipse[2]
    side = sum(size) / 2
    if side > min([image.shape[0], image.shape[1]]):
        side = min([image.shape[0], image.shape[1]])
    x1 = int(center[0] - side / 2)
    y1 = int(center[1] - side / 2)
    x2 = x1 + int(side)
    y2 = y1 + int(side)
    if int(center[0] - side / 2) < 0 or int(center[1] - side / 2) < 0:
        if int(center[0] - side / 2) < 0:
            x1 = 0
        else:
            x1 = int(center[0] - side / 2)
        if int(center[1] - side / 2) < 0:
            y1 = 0
        else:
            y1 = int(center[1] - side / 2)
        x2 = x1 + int(side)
        y2 = y1 + int(side)
    if int(center[0] + side / 2) > image.shape[1] or int(center[1] + side / 2) > image.shape[0]:
        if int(center[0] + side / 2) > image.shape[1]:
            x2 = image.shape[1]
        else:
            x2 = int(center[0] + side / 2)
        if int(center[1] + side / 2) > image.shape[0]:
            y2 = image.shape[0]
        else:
            y2 = int(center[1] + side / 2)
        x1 = x2 - int(side)
        y1 = y2 - int(side)
    
    if y1<20:  # move log
        y1=20
        
    clipped_image = np.array(image[y1: y2, x1: x2])
    #cv2.imshow('clip',clipped_image)
    resize_image = cv2.resize(clipped_image, (224, 224), interpolation=cv2.INTER_LANCZOS4)
    resize_image=clipped_image
    return resize_image

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




path='D:\\semester_4\\test_score'
file='1A_59.jpg'
save_dir='D:\\semester_4\\resultclip'
image=cv2.imread(os.path.join(path,file)) 
b, g, r = cv2.split(image)
cv2.imwrite(os.path.join(save_dir,'1.jpg'),r,[int(cv2.IMWRITE_JPEG_QUALITY),95])
binary_threshold_image = binary_threshold(r) #因为输入必须是黑白二值图像
cv2.imwrite(os.path.join(save_dir,'2.jpg'),binary_threshold_image,[int(cv2.IMWRITE_JPEG_QUALITY),95])
closed_opening_image = closed_opening_operation(binary_threshold_image) #效果：把非联通的断开，联通的合并
cv2.imwrite(os.path.join(save_dir,'3.jpg'),closed_opening_image,[int(cv2.IMWRITE_JPEG_QUALITY),95])
big_contour, red_mask = find_biggest_contour(closed_opening_image)  #big_contour:return 坐标位置    
red_mask_border=cv2.copyMakeBorder(red_mask,1,1,1,1,cv2.BORDER_CONSTANT,value=0)
binary_edge,clipped_image = edge(image, red_mask_border)
cv2.imwrite(os.path.join(save_dir,'4.jpg'),binary_edge,[int(cv2.IMWRITE_JPEG_QUALITY),95])
        #防止裁剪后照片已经小于224*224
cv2.imwrite(os.path.join(save_dir,'5.jpg'),clipped_image,[int(cv2.IMWRITE_JPEG_QUALITY),95])
height=clipped_image.shape[0]
width=clipped_image.shape[1]
if height<224 and width<224:
    pass
else:
    resize_image = cv2.resize(clipped_image, (224, 224), interpolation=cv2.INTER_LANCZOS4)          
    cv2.imwrite(os.path.join(save_dir,'6.jpg'),resize_image,[int(cv2.IMWRITE_JPEG_QUALITY),95])


'''
#扩充图像边界
path='E:\\zye\\test'
dirs=os.listdir(path)
for file in dirs:
    if os.path.splitext(file)[1] =='.jpg':
        print(file)
            
        image=cv2.imread(os.path.join(path,file)) 
        b, g, r = cv2.split(image)
       
        #cv2.imshow('xx',image)
        #cv2.imshow('r',r)
        
        #cv2.imshow('g',g)
        #cv2.imshow('b',b)
        binary_threshold_image = binary_threshold(r) #因为输入必须是黑白二值图像
        #cv2.imshow('threshold',binary_threshold_image)
        #cv2.waitKey()
        #cv2.destroyAllWindows()
        closed_opening_image = closed_opening_operation(binary_threshold_image) #效果：把非联通的断开，联通的合并
        #cv2.imshow('close_open',closed_opening_image)
        #cv2.waitKey()
        #cv2.destroyAllWindows()
        big_contour, red_mask = find_biggest_contour(closed_opening_image)  #big_contour:return 坐标位置        
        #print(big_contour)        
        #cv2.imshow('mask',red_mask)
        #cv2.waitKey()
        #cv2.destroyAllWindows()
        #扩充图像边界
        red_mask_border=cv2.copyMakeBorder(red_mask,1,1,1,1,cv2.BORDER_CONSTANT,value=0)
        #cv2.imshow('border',red_mask)
        #cv2.waitKey()
        #cv2.destroyAllWindows()
        binary_edge,resize_image = edge(image, red_mask_border)
        #save_dir='E:\\zye\\binary_edge'
        #cv2.imwrite(os.path.join(save_dir,file),binary_edge,[int(cv2.IMWRITE_JPEG_QUALITY),95])
        #cv2.imshow('edge_canny',edge)
        save_dir='E:\\zye\\after_zye_2'
        cv2.imwrite(os.path.join(save_dir,file),resize_image,[int(cv2.IMWRITE_JPEG_QUALITY),95])
        #save_dir='E:\\zye\\after_one'
        
        #cv2.imshow('clip',resize_image)
        #cv2.waitKey()
        #cv2.destroyAllWindows()
        
        #cv2.imwrite(os.path.join(save_dir,file),resize_image,[int(cv2.IMWRITE_JPEG_QUALITY),95])
'''
'''


path='E:\\zye\\test\\3A_a_1.jpg'
image=cv2.imread(path)
b, g, r = cv2.split(image)
        #cv2.imshow('xx',image)
        #cv2.imshow('r',r)
        #cv2.imshow('g',g)
        #cv2.imshow('b',b)
binary_threshold_image = binary_threshold(r) #因为输入必须是黑白二值图像
        #cv2.imshow('threshold',binary_threshold_image)
closed_opening_image = closed_opening_operation(binary_threshold_image) #效果：把非联通的断开，联通的合并
        #cv2.imshow('close_open',closed_opening_image)
big_contour, red_mask = find_biggest_contour(closed_opening_image)  #big_contour:return 坐标位置        
        #print(big_contour)        
cv2.imshow('mask',red_mask)
edge=cv2.Canny(red_mask,0,255)
cv2.imshow('edge',edge)
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

#resize_image = clip_resize_operation(image, big_contour)
#save_dir='E:\\zye\\after'
cv2.imshow('clip',clipped_image)
        
#cv2.imwrite(os.path.join(save_dir,file),resize_image,[int(cv2.IMWRITE_JPEG_QUALITY),95])
'''