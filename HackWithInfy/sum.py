

def sumFun(n,m):
    s=0
    for i in range(n,m+1,n):
        if i % n==0:
            s=s+i
    return s

def sumfun(n,m):
    l=[]
    i=n
    while i<=m:
        l.append(i)
        i+=n
    return l

n=int(input())
m=int(input())
print(sumfun(n,m))