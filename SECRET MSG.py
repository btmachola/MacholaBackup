# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 11:17:21 2025

@author: B MACHOLA
"""

m=int(input('enter a number'))
n=int(input('enter a 2nd number'))
def primesinrange(m,n):
    nf=[]
    for i in range(m,n+1):
        mf=[]
        for j in range (1,i+1):
            if (i%j==0):
                mf.append(j)
        if len(mf)==2:
            nf.append(i)
    return(nf)
row=primesinrange(100,300)
column=primesinrange(300,600)

import cv2
import numpy as np

img = cv2.imread('C:/Users/B MACHOLA/Desktop/cat.jpg')
b,g,r=cv2.split(img)

text = input ("type secret text")
l=len (text)
for i in range(0,l):
    img[row[i]][column[i]][0]=ord(text[i])
cv2.imwrite('C:/Users/B MACHOLA/Desktop/cat4.jpg',img)