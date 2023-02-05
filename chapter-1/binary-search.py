def binarySearch(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

myList = [1, 3, 5, 7, 9]
print(binarySearch(myList, 7)) # => 1

#Algorithms that uses binary search are faster than linear search
#because they eliminate half of the remaining items at every step.
#Binary search only works on sorted lists.
#If you're going to search an unsorted list, it's better to sort it first.
#Then you can do a binary search.
#Sorting is an algorithm that takes a list as input and returns a new sorted list.
#The Big O notation for binary search is O(log n).