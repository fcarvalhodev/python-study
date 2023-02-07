def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[0:4]), sum(arr[1:5]))

if __name__ == '__main__':
    miniMaxSum([1, 2, 3, 4, 5])