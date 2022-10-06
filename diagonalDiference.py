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
    resultadoA = 0
    resultadoB = 0
    aux = int(len(arr[0])) - 1
    for i in range(len(arr[0])):
        for j in range(len(arr[0])):
            if(j==i):
                resultadoA = resultadoA + arr[i][j]
                resultadoB = resultadoB + arr[i][aux-j]
    return abs(resultadoA-resultadoB)
    

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')

    
