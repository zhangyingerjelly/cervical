import cv2  #
#import matplotlib.pyplot as plt
import numpy as np
import os

def closed_opening_operation(image): #腐蚀与膨胀（作为寻找轮廓前的步骤）
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
    closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
    opening = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)

    return opening

path='D:\\semester_4\\detection\\HSL'
file='4-57.jpg'
save_dir='D:\\semester_4\\detection\\detect'
image=cv2.imread(os.path.join(path,file)) 
#b, g, r = cv2.split(image)

gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('border',gray)
cv2.waitKey()
cv2.destroyAllWindows()

_,ret=cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY) #阈值还可以再改
cv2.imshow('border',ret)
cv2.waitKey()
cv2.destroyAllWindows()

closed_opening_image = closed_opening_operation(ret) #效果：把非联通的断开，联通的合并
cv2.imwrite('1.jpg',closed_opening_image,[int(cv2.IMWRITE_JPEG_QUALITY),95])
cv2.imshow('border',closed_opening_image)
cv2.waitKey()
cv2.destroyAllWindows()


edge=cv2.Canny(closed_opening_image,0,255)
print(edge)
cv2.imwrite('2.jpg',edge,[int(cv2.IMWRITE_JPEG_QUALITY),95])
cv2.imshow('border',edge)
cv2.waitKey()
cv2.destroyAllWindows()


COLORS=[60,122,50]
print(COLORS)
edge_m=np.zeros_like(image) #3通道
cord=np.where(edge==255)
edge_m[cord]=COLORS

new=edge_m+image
cv2.imshow('bord',new)
cv2.waitKey()
cv2.destroyAllWindows()


image = np.float32(image) / 255.0
gx = cv2.Sobel(image,cv2.CV_32F,1,0,3)
gy = cv2.Sobel(image,cv2.CV_32F,0,1,3)
mag, angle = cv2.cartToPolar(gx, gy)
print(mag.shape)
cv2.imshow('bord',mag)
cv2.waitKey()
cv2.destroyAllWindows()

'''
cv2.imshow('bord',mag[:,:,0])
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('bord',mag[:,:,1])
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('bord',mag[:,:,2])
cv2.waitKey()
cv2.destroyAllWindows()
'''

mag[:,:,0]=np.where(mag[:,:,0]>0.25,1.0,0)
cv2.imshow('bord',mag[:,:,0])
cv2.waitKey()
cv2.destroyAllWindows()

closed_opening_image = np.float32(closed_opening_image) / 255.0
newdot=cv2.bitwise_and(mag[:,:,0],closed_opening_image)
cv2.imshow('n',newdot)
cv2.waitKey()
cv2.destroyAllWindows()
COLORS=[1,0,0]
dot=np.zeros_like(image) #3通道
cord=np.where(newdot==1.0)
dot[cord]=COLORS

new=np.float32(new) / 255.0
new=dot+new
cv2.imwrite('detect.jpg',new,[int(cv2.IMWRITE_JPEG_QUALITY),95])
cv2.imshow('bord',new)
cv2.waitKey()
cv2.destroyAllWindows()
