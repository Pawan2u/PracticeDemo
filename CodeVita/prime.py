
def isPrime(n):
    if n%2==0:
        return "Not"
    if n<2:
        return "Not"
    i=2
    while i*i <= n:
        if n%i==0:
            return "Not"
        i+=1
    return "Yes"




n=100
print(isPrime(n))