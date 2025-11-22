# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 00:39:01 2025

@author: B MACHOLA
"""

def partition(arr, left, right):
    pivot = arr[right]  # Choose last element as pivot
    i = left        # Index of smaller element
    j=right-1

    
    while i<j:
        while i<right and arr[i]<pivot:
            i+=i
        while j >left and arr[j]>pivot:
            j-=1
        print(i)
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]  # Swap
            
    if arr[i]>pivot:
        arr[i], pivot  = pivot, arr[i]  # Final pivot swap
   
    return i 

def quicksort(arr, low, high):
    if low < high:
        pivot_pos = partition(arr, low, high)

        quicksort(arr, low, pivot_pos - 1)   # Left of pivot
        quicksort(arr, pivot_pos + 1, high)  # Right of pivot

# Example usage
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
