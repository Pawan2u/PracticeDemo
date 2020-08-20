
''' Prime Sieve
   

 '''
def prime_sieve(n):
    prime=[True for i in range(n+1)] 
    p=2
    while p*p<=n:
        if prime[p]==True:
            for i in range(p*2,n+1,p):
                prime[i]=False
        p+=1
    prime[0]=False
    prime[1]=False
    for i in range(n+1):
        if prime[i]==True:
            print(i,end=' ')


n=int(input())
print(prime_sieve(n))