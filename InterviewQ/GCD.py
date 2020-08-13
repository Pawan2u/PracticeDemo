
def gcd1(a,b):
    """Euclid Formula """
    while b>0:
        temp=a
        a=b
        b=temp%a
    return a

def gcd2(a,b):
    '''
    if a<b:
        small=a
    else:
        small=b
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd
    
    '''
    #Best as complexity reverse Traverse.....#
    small= a if a<b else b
    for i in range(small,0,-1):
        if a%i==0 and b%i==0:
            return i
  
def gcd3(a,b):
    if b==0:
        return a
    else:
        return gcd3(b,a%b)


a,b=map(int,input("Enter num:").split())
print(f'GCD of {a},{b} is {gcd3(a,b)}')