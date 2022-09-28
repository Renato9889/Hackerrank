import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    resultado = [0.0,0.0,0.0]
    cont1 = 0
    cont2 = 0
    cont3 = 0
    for i in range(len(arr)):
        if(arr[i]>=1):
            cont1 = cont1 + 1
        else:
            if(arr[i]<=-1):
                cont2 = cont2 + 1
            else:
                if(arr[i]==0):
                    cont3 = cont3 + 1
    print(cont1/len(arr))
    print(cont2/len(arr))
    print(cont3/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
