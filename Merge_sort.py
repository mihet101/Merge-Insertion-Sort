'''
Merge_Insertion Sort
Merge Sort
Insertion Sort
Author: Mihe3200
ID: 180963200
Email: mihe3200@mylaurier.ca
'''
from Insertion_sort import *

def merge_sort(array):

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)

def insertionSort(A): 

    #print(" ",A) 
    print("\nInsertion sorting: ",A) 

    for j in range(1, len(A)):   

        key = A[j] 

        i = j-1

        while i >= 0 and A[i] > key: 

            A[i + 1] = A[i] 

            i = i - 1

            #print("\n ", A)

        A[i + 1] = key

        #print("\n ",A)
    print(A)
    return A

def merge_insertion_sort(array, user_level, level=1):

    if level == user_level:  # base case
        new_array = insertionSort(array)
        return new_array
    
    # divide array in half and merge sort recursively
    level += 1
    half = len(array) // 2
    left = merge_insertion_sort(array[:half],user_level, level)
    right = merge_insertion_sort(array[half:],user_level, level)
    
    return merge(left, right)
