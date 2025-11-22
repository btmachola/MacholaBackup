# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 11:08:05 2025

@author: B MACHOLA
"""

def bubble_sort(L):
    size = len(L)
    for i in range(0,size-1):
        count=0
        for j in range(0,size-1-i):
            if L[j]>L[j+1]:
                tmp=L[j]
                L[j]=L[j+1]
                L[j+1]=tmp
                count=count+1
        #check if sort is complete
        if count==0:
            break
L=[3,9,1,7,10,2,13,2]
bubble_sort(L)
print(L)
                