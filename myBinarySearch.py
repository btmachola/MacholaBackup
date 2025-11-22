# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 22:32:09 2025

@author: B MACHOLA
"""

def BinarySearch(arr,target):
    l=0
    r=len(arr)
    
    while l< r :
        mid=(l+r)//2
        if arr[mid]==target:
            return mid
            
        elif arr[mid]<target:
            l=mid+1
            print("the mid is",mid)            
        else:
            r=mid
            print("the mid is",mid) 
    print("the target  is not found")    
    return -1      

nums=[1,2,3,9,13,17]
x=BinarySearch(nums, 17)
print("the target  is at", x)  