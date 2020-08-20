def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact(n-1)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact


n=int(input("Enter a num:"))
print(factorial(n))