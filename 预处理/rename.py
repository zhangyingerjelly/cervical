# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
target_dir='E:\\zye\\origin_data\\A\\ONE\\6'
filelist=os.listdir(target_dir)
i=1
for file in filelist:
    new_name='6A_'+str(i)+'.jpg'
    #print(new_name)
    os.rename(os.path.join(target_dir, file),
              os.path.join(target_dir, new_name))
    i +=1
