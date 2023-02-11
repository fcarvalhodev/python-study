#!/bin/python3

import math
import os
import random
import re
import sys

def lonelyinteger(a):
    return (sum(set(a)) * 2 - sum(a))


if __name__ == '__main__':
    result = lonelyinteger([1, 2, 3, 4, 3, 2, 1])


#The code is a function that returns the only element in an array that does not have a pair.
#Time complexity is O(n) as the function needs to traverse all elements in the worst-case scenario.
#Space complexity is O(n) as well, as it needs to store the calls to the function in the call stack.

#In this code, set is used to remove duplicates from the nums array. The sum of unique elements is then multiplied by
# 2, and the result is subtracted from the sum of the original nums array. The resulting value is the element that
# appears only once in the array.
