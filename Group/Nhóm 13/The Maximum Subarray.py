#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    if max(arr)<0:
        return(max(arr),max(arr))
    a=0
    best_sum = 0  
    current_sum = 0
    for i in arr:
        if i>0:
            a+=i

        current_sum = max(0, current_sum + i)
        best_sum = max(best_sum, current_sum)
    
    return best_sum,a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
