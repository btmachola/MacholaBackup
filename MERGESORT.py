# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 10:50:43 2025

@author: B MACHOLA
"""

#Merge sort
arr=[]
el1=[1, 3, 9, 47, 87, 64, 100]
el2=[8,19,41,76,80,91,98]

def MergeSort(el1,el2,arr):
    
    len_a=len(el1)
    len_b=len(el2)
    i=j=k=0
    
    
    
    while i<len_a and j<len_b:
        if el1[i]<=el2[j]:
            arr.append(el1[i])
            i+=1
        else:
            arr.append(el2[j])
            j+=1
            
#add remaining elements
            
    while i<len(el1):
         arr.append(el1[i])  
         i+=1
         
    while j<len(el2):
            arr.append(el2[j])
            j+=1
MergeSort(el1, el2, arr)
print(arr)