# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 11:40:43 2020

@author: Dell
"""
import cv2
import os
path='E:\\zye\\after_origin_data\\three_zicai'
save_dir='E:\\zye\\after_origin_data\\THREE'
dirs=os.listdir(path)
for file in dirs:
    if os.path.splitext(file)[1] =='.jpg':
        print(file)            
        image=cv2.imread(os.path.join(path,file)) 
        resize_img=cv2.resize(image, (224, 224), interpolation=cv2.INTER_LANCZOS4)
        cv2.imwrite(os.path.join(save_dir,file),resize_img,[int(cv2.IMWRITE_JPEG_QUALITY),95])