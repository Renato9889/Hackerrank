import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    cont1 = 0
    cont2 = 0
    for i in range(4):
        cont1 = cont1 + arr[i]
        cont2 = cont2 + arr[i+1]
    
    print(cont1,cont2)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
