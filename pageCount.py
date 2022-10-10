import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#
def pageCount(n, p):
    cont_inicio = p//2
    cont_final = (n//2) - (p//2)
    return min(cont_inicio,cont_final)
 

if __name__ == '__main__':

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(str(result) + '\n')
