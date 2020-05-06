# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:38:34 2019

@author: Dell
"""

import time
import os
from PIL import Image
import numpy as np
start =time.time()
target_dir='E:\\zye\\origin_data\\A\\ONE\\6'
filelist=os.listdir(target_dir)
lib=[]
flag=0
for filename in filelist:
    img=Image.open(os.path.join(target_dir, filename))    
    r,g,b=img.split()
    r_array = np.array(np.array(r, dtype=np.uint8)).flatten()
    r_list=r_array.tolist()
    
    if r_list in lib:
        os.remove(os.path.join(target_dir,filename))
        flag=1
    else:
        lib.append(r_list)
    
print(flag)
    
end = time.time()

print('Running time: {} Seconds'.format(end-start))    
del lib,filelist