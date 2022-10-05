import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    newhora = [0,0,0,0,0,0,0,0]
    ap = s[8]
    for i in range(8):
        newhora[i] = s[i]    
    
    if(ap=="A" and newhora[1]=="2"):
        newhora[0] = str(0)
        newhora[1] = str(0)    
    if(ap=="P"):
      if(newhora[1]=="2" and newhora[0]=="1"):
        newhora[1] = "2"
      else:
        listaaux = [newhora[0],newhora[1]]
        aux = int("".join(map(str, listaaux)))
        aux = aux + 12
        unidade = aux%10
        aux = (aux-unidade)/10
        dezena = aux%10      
        newhora[0]=str(int(dezena))
        newhora[1]=str(unidade)
            
    resultado = "".join(newhora)
    return resultado

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result + '\n')

