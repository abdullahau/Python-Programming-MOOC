# Sorting Algorithms
# A sorting algorithm is a method or a process used to rearrange elements in a list or an array in a 
# certain order, whether it be ascending, decending, or even based on some complex rules.

# Bubble Sort
# Bubble sort is a simple sorting algorithm that repeatedly steps through the array, element by element
# comparing the current element with the one after it, swapping their values if the former is larger than the latter.
arr = [12, 20, 15, 29, 10, 14]

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

bubbleSort(arr)
print(arr)

# Insertion Sort
# Insertion sort is a simple sorting algorithm that builds the final sorted array one element at a time
arr = [13, 20, 7, 28, 3, 8]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertionSort(arr)
print(arr)

# Merge Sort
# Merge sort is an efficient, stable, and comparison-based Divide and Conquer sorting algorithm, and its recursive.
# It divides the input array into two halves, calls itself for the halves, sorting them and then merges the two sorted halves.
arr = [39, 45, 45, 29, 50, 48, 41, 18, 14, 22, 27]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        merge(arr, L, R)

def merge(arr, L, R):
    i = j = k = 0
    
    # Merging the temporary arrays
    # back into arr[]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Copy the remaining elements
    # of L[], if there are any
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
        
    # Copy the remaining elements 
    # of R[], if there are any
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        
merge_sort(arr)
print(arr)

# Other sorting alcorithms:
# Selection, Shell, Heap, Quick and Quick3


# Searching Algorithms
# A searching algorithm is a method or process used to find or retrieve an element from a data structure.
# The goal is to find whether an item exists in the data set, and oftentimes to determine its location.

# Linear Search
# Each element is checked in sequence until you find what you're looking for or the list ends.
# If the current element equals what we're looking for (x), return it. 

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

print(linear_search(arr, 8))
arr[linear_search(arr, 8)]

# Binary Search
# Binary Search works by repeatedly dividing in half the portion of the list that could contain the item, 
# until you've narrowed down the possible location to just one.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print(linear_search(arr, 8))
arr[linear_search(arr, 8)]

# Binary Search - 2

def binary_search(target: list, item: int, left : int, right : int):
    """ The function returns True if the item is contained in the target list, False otherwise """
    # If the search area is empty, item was not found
    if left > right:
        return False

    # Calculate the centre of the search area, integer result
    centre = (left+right)//2

    # If the item is found at the centre, return
    if target[centre] == item:
        return True

    # If the item is greater, search the greater half
    if target[centre] < item:
        return binary_search(target, item, centre+1, right)
    # Else the item is smaller, search the smaller half
    else:
        return binary_search(target, item, left, centre-1)

target = [1, 2, 4, 5, 7, 8, 11, 13, 14, 18]
print(binary_search(target, 2, 0, len(target)-1))
print(binary_search(target, 13, 0, len(target)-1))
print(binary_search(target, 6, 0, len(target)-1))
print(binary_search(target, 15, 0, len(target)-1))
