import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    for i in range(len(a)):
        b = a.count(a[i])
        if(b == 1):
            return a[i]

if __name__ == '__main__':
    
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(str(result) + '\n')
