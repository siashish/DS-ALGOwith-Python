from math import sqrt

def checkprime(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count+=1

    if count == 2:
        print("prime number")
    else:
        print("not a prime number")

def checkprime2(n):
    count =0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            print("not a prime number")
            return
    print("prime number")
    return

checkprime2(7)
checkprime2(10)
