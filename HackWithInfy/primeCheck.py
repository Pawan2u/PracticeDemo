import math
import time

def checkPrime1(n):
    
    if n==1:
        return str(n)+" Not Prime"
    for i in range(2,n):
        if n%i==0:
            return str(n)+" Not Prime"
    return str(n)+" Prime"

def checkPrime2(n):

    if n==1:
        return str(n)+" Not Prime"
    
    max_div=math.floor(math.sqrt(n))
    for i in range(2,max_div+1):
        if n % i==0:
            return str(n)+"Not Prime"
        return str(n)+" Prime"

def checkPrime3(n):

    if n==1:
        return False
    
    if n==2:
        return True
    if n>2 and n%2==0:
        return False
    
    max_div=math.floor(math.sqrt(n))
    for i in range(3,max_div+1,2):
        if n%i==0:
            return False
    return True
    





n=int(input("Enter num:"))
"""
t0=time.time()
for i in range(2,n):
    print(checkPrime1(i))
t1=time.time()
k=t1-t0
print("Time taken: ",t1-t0)
"""
"""
t2=time.time()
for i in range(2,n):
    print(checkPrime2(i))
t3=time.time()
l=t3-t2
print("Time taken: ",t3-t2)
"""


t4=time.time()
for i in range(2,n):
    print(i,checkPrime3(i))
t5=time.time()
print("Time taken:",t5-t4)

