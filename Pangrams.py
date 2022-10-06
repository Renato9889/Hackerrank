import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alfaBeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    s = s.upper()
    cont = 0
    for i in range(len(alfaBeto)):
        for j in range(len(s)):
            if(alfaBeto[i]==s[j]):
                cont +=1
                break
    if(cont == 26O ):
        return "pangram"
    else:
        return "not pangram"
if __name__ == '__main__':

    s = input()

    result = pangrams(s)

    print(result + '\n')

