#Scott Dickson
#Practice writing sorting algorithms

import random

#Also as expected
def quicksort(arr):
    n = len(arr)
    if n == 1 or n == 0:
        return arr
    elif n == 2:
        return arr if arr[1] > arr[0] else [arr[1],arr[0]]
    else:
        splitter = arr[random.randrange(n)]
        right = []
        left = []
        
        for i in range(n):
            if arr[i] > splitter:
                right.append(arr[i])
            else:
                left.append(arr[i])
        return quicksort(left)+quicksort(right)
        
        
#As expected 
def mergesort(arr):
    n = len(arr)
    if n == 1 or n == 0:
       return arr
    elif n == 2:
        return arr if arr[1] > arr[0] else [arr[1],arr[0]]
    else:
        splitter = n // 2 
        left = mergesort(arr[0:splitter])
        right = mergesort(arr[splitter:])
        return merge(left,right)
        
#Merge two sorted lists and return the result
def merge(arr1, arr2):
    merged = []
    
    while arr1 != [] and arr2 != []:
        if(arr1[len(arr1) - 1] > arr2[len(arr2) - 1]):
            merged = [arr1.pop()] + merged
        else:
            merged = [arr2.pop()] + merged
    
    return arr1 + arr2 + merged
    
    

if __name__ == '__main__':
    lst1 = [1,4,6,2,3,4,5,9,8,3,10]
    lst2 = [4,5,5,6,10]
    print(lst1)
    print(lst2)
    print(quicksort(lst1))
    print(mergesort(lst1))
    
    