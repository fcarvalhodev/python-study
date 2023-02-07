def plusMinus(arr):
    arr.sort()
    arrSize = len(arr)
    positive_numbers = len([num for num in arr if num > 0])
    negative_numbers = len([num for num in arr if num < 0])
    zeros = len([zero for zero in arr if zero == 0])
    print(positive_numbers / arrSize)
    print(negative_numbers / arrSize)
    print(zeros / arrSize)

if __name__ == '__main__':
    plusMinus([1, 1, 0, -1, -1])