# The Big O notation for quicksort is O(n log n).
# This is because the algorithm divides the array in half at each iteration.
# The algorithm is also recursive, so it needs to store the calls in the call stack.

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))