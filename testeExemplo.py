def fizzBuzz(n):
    for i in range(n+1):
        if(i>0):
            if(i%3==0):
                print("Fizz",end="")
            if(i%5==0):
                print("Buzz",end="")
            if(i%3!=0 and i%5!=0):
                print(i,end="")
        print()
    
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
1