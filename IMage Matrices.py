# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 09:36:51 2025

@author: B MACHOLA
"""

import numpy as np
import cv2

img =cv2.imread('C:/Users/B MACHOLA/Desktop/cat.jpg')
img1 =cv2.imread('C:/Users/B MACHOLA/Desktop/cat.jpg')
b,g,r =cv2.split(img)


#for i in range(1200,1400):
   # for j in range (1600,2100):
       # img[i][j]=np.array([0,0,0])
       #change color
      # img[i][j]=np.array([[img[i][j][0],0,0]])
  #invert image
for i in range(0,1399):
    for j in range (0,2099): 
        img1[i][j]=img[1399-i][2099-j]
        
#rotate 90 deg
b=b.T
g=g.T
r=r.T
img3=cv2.merge([b,g,r])
cv2.imwrite('C:/Users/B MACHOLA/Desktop/cat5.jpg',img3)
        
    
        