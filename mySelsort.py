# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 18:31:30 2025

@author: B MACHOLA
"""


def selsort(nums):
    for i in range (len(nums)):
        print ("i=",i)
        minpos=i
        for j in range (i+1):
            print(j)
            
            if nums[j]<nums[minpos]:
                minpos=j
                
        t=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=t
            
       
    
nums=[5,2,9,11,3,1]
selsort(nums)
print(nums)