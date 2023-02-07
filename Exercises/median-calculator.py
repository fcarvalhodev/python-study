def findMedian(arr):
    n = len(arr)
    s = sorted(arr)
    if (n % 2 == 1):
        return s[n//2]
    else:
        return (s[n//2 - 1] + s[n//2])/2

if __name__ == '__main__':
    result = findMedian([0, 1, 2, 4, 6, 5, 3])
    print(result)


#The time complexity of this code is O(n * log(n)) because the sorting algorithm used in the sorted function
#takes O(n * log(n)) time to sort an array of n elements. This is because the sorted function uses
#the Timsort algorithm, which is a combination of merge sort and insertion sort that is optimized for real-world data.
#The space complexity of this code is O(n) because the sorted array created by the sorted function
#takes up O(n) space in memory. The original array and the rest of the variables used in the
#function take up additional space, but the majority of the space usage is due to the sorted array.
#The operator // is the floor division operator in Python. It returns the integer result of
#dividing the first number by the second number, rounded down to the nearest integer. For example, 7 // 2 would return 3, and -7 // 2 would return -4.
#The expression (s[n//2 - 1] + s[n//2])/2 calculates the average of the two middle elements of
#the sorted array s. If the number of elements in the array is odd, n//2 is the index of the middle element,
#so the median is just s[n//2]. If the number of elements in the array is even, n//2 is the index of the first of
#the two middle elements, so the median is the average of these two elements, calculated as (s[n//2 - 1] + s[n//2])/2.
