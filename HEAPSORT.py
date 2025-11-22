# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 09:59:36 2025

@author: B MACHOLA
"""

#HEEAP SORT
def heapify(arr,n,i):
    largest= i
    l=2*i+1
    r=2*i+2
    
    if l<n and arr[i]<arr[l]:
        largest =l
        if r<n and arr[largest]<arr[r]:
            largest=r
        if largest !=i:
            (arr[i], arr[largest]) = (arr[largest],arr[i])
            heapify(arr,n,largest)
            
def heapSort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
        
    for i in range(n-1,0,-1):
        (arr[i],arr[0])=(arr[0],arr[i])
        heapify(arr,i,0)
        
a=[100,9,87,3,47,1,64]
heapSort(a)
print(a)