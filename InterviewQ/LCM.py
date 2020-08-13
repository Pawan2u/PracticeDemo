
def lcm(a,b):
    large=a if a>b else b
    for i in range(1,large+1):
        l=large*i
        if l%a==0:
            return l


""" LCM x HCF = a x b """
def gcd(a,b):
    if b==0:
        return a
    return gcd(a,a%b)          
def lcm2(a,b):
    return (a*b)/gcd(a,b)




a,b=map(int,input("Enter num:").split())
print(f'LCM of {a} and {b} is {int(lcm2(a,b))}')