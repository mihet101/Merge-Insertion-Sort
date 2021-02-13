'''
Created on 2021 Feb 6

@author: timothy
'''
from Merge_sort import *

#tree_level = input("Enter tree_level: ")
tree_level = int(input("Enter tree_level: "))
A = list(map(int,input("\nEnter the numbers: ").strip().split()))
print("\nstarting array: ", A)
result = merge_insertion_sort(A,tree_level)

print()
print("Sorted List: ", result)
