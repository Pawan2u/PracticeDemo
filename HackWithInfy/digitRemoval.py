""" Two consecutive num sum= 17 remove digit from number again check num if consecutive two digit sum=17 again and again
    If not found then print digit and count of number

    Like 5678901
            here 8+9=17
        so 56701
            here not possible

        number is 56701
        digit count=5
"""

def digitCount(num):
    a,b=0,0
    re=False
    l=[]
    l1=""
    for i in num:
        l.append(int(i))
    for i in range(len(l)-1):
        if l[i]+l[i+1]==15:
            re=True
            a,b=i,i+1
    if re==True:
        del l[a:b+1:1]
        print(l)
        for i in l:
            l1+=str(i)
        return digitCount(l1)
    else:
        return len(l)
    
    

    
n="69678969"
print(digitCount(n))