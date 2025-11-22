# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 22:49:01 2025

@author: B MACHOLA
"""

def heapify(arr,n,i):
    
    largest=i
    l=2*i
    r=2*i+1
    
    if l<n and arr[l]>arr[i]:
        largest=l
          
    if r<n and arr[r]>arr[largest]:
        largest=r
        
    if largest !=i : #parent is not larger
        t=arr[i]                 #swap
        arr[i] =arr[largest]
        arr[largest]=t
        
        heapify(arr,n,largest) #repeat for the other child
        
def Hsort(arr):
    n=len(arr)
    #heapify all from bottom sub trees
    for i in range (n//2,-1,-1):
        print ("i=",i)
        heapify(arr,n,i)
        
    #drop largest then heapify
    for i in range (n-1,0,-1):
      #swap     top with last 
      t=arr[0]
      arr[0] =arr[i]
      arr[i]=t
      
      heapify(arr,i,0)       
      #drop it from the sort by moving to net i     
       
    
nums=[5,2,9,11,3,1]
Hsort(nums)
print("heap sorted is", nums)