import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    artempo = sorted(set(ar))
    cont = 0
    for i in range(len(artempo)):
        x = ar.count(artempo[i])
        if(x>0):
            if(x%2!=0):
                x = x-1
            cont += int(x/2)
    return cont

if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')

