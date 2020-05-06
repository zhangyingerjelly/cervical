import cv2
import matplotlib.pyplot as plt
#from glob import glob
import numpy as np
import os
import json

## score under 150 is blur
## 模糊检测（根据拉普拉斯变换后高低频分量）
def blur_detect(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    score = cv2.Laplacian(gray_image,ddepth=-1,ksize=3).var()
    return score




target_dir='D:\\semester_4\\test_score'
filelist=os.listdir(target_dir)
print(filelist)
with open ('blur.txt','w') as f:
    for filename in filelist:
        img=cv2.imread(os.path.join(target_dir, filename))
        print(img.shape)
        score=blur_detect(img)
        
        string=filename+'   '+str(score)+'\n'
        print(string)
        f.write(string)