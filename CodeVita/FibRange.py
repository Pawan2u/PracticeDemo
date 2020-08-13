def fibRange(first,second,n):
    a=first
    b=second
    if n==1:
        return a
    elif n==2:
        return b
    else:
        for i in range(3,n+1):
            c=a+b
            a=b
            b=c
        return b




first,second=0,1
n=12
print(fibRange(first,second,n))