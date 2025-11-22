# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 11:32:47 2025

@author: B MACHOLA
"""

#QUICK SORT

def swap(a,b,arr):
    if a!=b:
        temp=arr[a]
        arr[a]=arr[b]
        arr[b]=temp
def quick_sort(elements,start ,end):
    if start<end:
        pi=partition(elements,start ,end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1 ,end)

        
def partition(elements,start,end):
    pivot_index=start
    pivot=elements[pivot_index]
    
    while start<end:
        while start<len(elements) and elements[start]<=pivot:
            start+=1
        while elements[end]>pivot:
            end-=1
        if start<end:
            swap(start,end,elements)
    swap(pivot_index,end,elements)
    return end
elements=[3,8,1,0,78,23,90]
quick_sort(elements, 0, len(elements)-1)
L=[3,9,1,7,10,2,13,2]
quick_sort(L,0,len(L)-1)
