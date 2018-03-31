#!/usr/bin/python 2

# Complete the function below.

def getProductArray(nums):
    n = len(nums)
    up = [None] * n
    down = [None] * n
    
    for i, element in enumerate(nums):
        up[i] = up[i-1]*element if i != 0 else element
        j = n-i-1
        down[j] = down[j+1]*nums[j] if j != n-1 else nums[j]
    
    print('up', up)
    print('down', down)
    
    result = [None] * n
    for i in range(n):
        if i == 0:
            result[0] = down[1]
        elif i == n-1:
            result[n-1] = up[n-2]
        else:
            result[i] = up[i-1]*down[i+1]
    
    return result
    

