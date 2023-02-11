#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    main_total = 0
    secondary_total = 0
    for i in range(len(arr)):
        main_total += arr[i][i]
        secondary_total += arr[i][len(arr) - 1 - i]
    return abs(main_total - secondary_total)

if __name__ == '__main__':
    result = diagonalDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(result)


#The code is a function that returns the absolute difference between the sums of the main and secondary diagonals of
# a square matrix.
#Time complexity is O(n) as the function needs to traverse all elements in the worst-case scenario.
#Space complexity is O(1) as it does not need to store any data in memory.