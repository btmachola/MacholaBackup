# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 08:38:57 2025

@author: B MACHOLA
"""


def bsort(nums):
    for i in range (len(nums)-1,0,-1):
        print ("i=",i)
        for j in range (i):
            print("j=",j)
            
            if nums[j]>nums[j+1]:
                t=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=t
            print(nums)
       
    
nums=[5,2,9,11,3,1]
bsort(nums)
print(nums)