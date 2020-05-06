import cv2
import matplotlib.pyplot as plt
#from glob import glob
import numpy as np
import os
import json

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
    cv2.imwrite('2.jpg',mask,[int(cv2.IMWRITE_JPEG_QUALITY),95])
    cv2.imshow('mask',mask)
    cv2.waitKey()
    cv2.destroyAllWindows()
    kernel=np.ones((5,5),np.uint8)
    mask=cv2.dilate(mask,kernel)
    cv2.imshow('mask',mask)
    cv2.imwrite('3.jpg',mask,[int(cv2.IMWRITE_JPEG_QUALITY),95])
    cv2.waitKey()
    cv2.destroyAllWindows()
    #dst=np.zeros([147,186])
    #dst=cv2.illuminationChange(img,mask,alpha=0.2,beta=0.4)
    dst=cv2.inpaint(img,mask,20,cv2.INPAINT_NS)
    #效果很不错，比illumination好
    return dst
    
path='1A_115.jpg'    
image=cv2.imread(path)
print(image)
print(image.shape)
print(image.dtype)
mask=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('1.jpg',mask,[int(cv2.IMWRITE_JPEG_QUALITY),95])



image_after=reflect(image)
cv2.imwrite('4.jpg',image_after,[int(cv2.IMWRITE_JPEG_QUALITY),95])
cv2.imshow('mask',image_after)
cv2.waitKey()
cv2.destroyAllWindows()