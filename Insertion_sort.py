'''
Created on 2021 Feb 4

@author: timothy
'''

def insertionSort(A): 

    #print(" ",A) 
    print("\ninsertion sorting: ",A) 

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