
def isPrime(n):
    if n%2==0:
        return False
    if n<2:
        return False
    i=2
    while i*i <= n:
        if n%i==0:
            return False
        i+=1
    return True

D,P=map(int,input().split())
H=D//P
N=H
result=0

while N>1:
    i=0
    count=0
    while True:
        k=(i*H)+N
        print(i,H,N,k)
        if isPrime(k) and k<=D:
            count+=1
        if i==P-1:
            break
        i+=1
    if count==P:
        result+=1
    N-=1
print(result,end="")