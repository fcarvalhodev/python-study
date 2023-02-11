# The Big O notation for selection sort is O(n^2).
# This is because there are two nested loops.
# The first loop goes through n elements.
# The second loop also goes through n elements for each iteration of the first loop.

def smallSearch(arr):
    minor = arr[0]
    minor_index = 0
    for i in range(1, len(arr)):
        if arr[i] < minor:
            minor = arr[i]
            minor_index = i
    return minor_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        minor = smallSearch(arr)
        newArr.append(arr.pop(minor))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))