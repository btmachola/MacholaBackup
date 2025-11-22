# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 08:45:09 2025

@author: B MACHOLA
"""

#Merge sort 2
arr=[]
#a=[1, 3, 9, 47, 87, 64, 100]
#b=[8,19,41,76,80,91,98]

def MergeSort(arr):
     if len(arr)<= 1:
       return
   
     mid=len(arr)//2
     left=arr[:mid]
     right=arr[mid:]
    
     MergeSort(left)
     MergeSort(right)
     merge_two_sorted_lists(left,right,arr)
     
def merge_two_sorted_lists(a,b,arr):
     Len_a= len(a)
     Len_b= len(b)
     i=j=k=0
     
     while i<Len_a and j<Len_b:
        if a[i]<=b[j]:
            arr[k]=a[i]
            i+=1
        else:
           arr[k]=b[j]
           j+=1
        k=k+1 
#add remaining elements
            
     while i<len(a):
         arr[k]=a[i]  
         i+=1
         k+=1
     while j<len(b):
         arr[k]=b[j]
         j+=1 
         k+=1
     print(arr)