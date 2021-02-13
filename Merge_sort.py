'''
Merge and Merge_Insertion Sorts

'''

from Insertion_sort import *

def merge(left, right):

    print("\nmerging: ", left, " and ", right)
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    
    print(result)
    return result


def merge_sort(array):

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)



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
