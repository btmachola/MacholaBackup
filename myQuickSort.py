# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 23:50:23 2025

@author: B MACHOLA
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    pivot = arr[-1]  # Choose the last element as pivot
    left = [x for x in arr[:-1] if x < pivot]
    right = [x for x in arr[:-1] if x >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
