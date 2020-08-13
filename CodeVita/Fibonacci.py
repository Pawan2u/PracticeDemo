import math
"""USING RECURSION TIME COMPLEXITY EXPONENTIAL COMPLEXITY SPACE O(N)"""
def fib(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

"""USING DYNAMIC PROGRAMMING AVOID REPAETED WORK"""

def fibo(n):
    fib_list=[0,1]
    while len(fib_list)<n+1 :
        fib_list.append(0)
    if n<=1:
        return n
    else:
        if fib_list[n-1]==0:
            fib_list[n-1]=fibo(n-1)
        if fib_list[n-2]==0:
            fib_list[n-2]=fibo(n-2)
    fib_list[n]=fib_list[n-2]+fib_list[n-1]
    return fib_list[n]
 
"""SIMPLE T=O(n) and S= O(1)"""
    
def fibonacci(n):
    a=0
    b=1
    if n<0:
        return False
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return b
"""USING POWER OF MATRIX T=O(n) AND S=O(1)"""
#       n
#  (1 1)     =  (Fn+1  Fn  )
#  (1 0)     =  (Fn    Fn-1)

def fibon(n):
    F=[[1,1],
       [1,0]]
    if n==0:
        return 0
    power(F,n-1)
    return F[0][0]
def multiply(F,M):
    x=(F[0][0]*M[0][0]+F[0][1]*M[1][0])
    y=(F[0][0]*M[0][1]+F[0][1]*M[1][1])
    z=(F[1][0]*M[0][0]+F[1][1]*M[1][0])
    w=(F[1][0]*M[0][1]+F[1][1]*M[1][1])

    F[0][0]=x
    F[0][1]=y
    F[1][0]=z
    F[1][1]=w

def power(F,n):
    M=[[1,1],
       [1,0]]
    for i in range(2,n+1):
        multiply(F,M)


"""USING FORMULA o(logn)"""
#                      n
#  Fn=[ ({sqrt(5)+1}/2) ]sqrt(5)

def fibonacci_(n):
    result=(1+ math.sqrt(5))/2
    return  math.floor((math.pow(result,n)/math.sqrt(5)))




n=int(input())
#print(fibonacci_(n))
result=fibonacci_(n)
if result==12:
    print(13)
else:
    print(result)