
def fun(n1,n2):
    count=0
    while n1>0 or n2 >0:
        num1,num2=n1,n2
        if n1>0:
            rem1 = num1 % 10
        else:
            rem1=0
        if n2>0:
            rem2= num2 % 10
        else:
            rem2=0
        p = rem1 + rem2
        carry = p % 10
        if p > 9:
            count += 1
            s = rem1 + rem2 + carry
        else:
            s= rem1 + rem2
        
        if n1>0:
            n1 = int(n1/10)
        if n2>0:
            n2 = int(n2/10)
    return count



n1=int(input("Enter num:"))
n2=int(input("Enter num:"))
print(fun(n1,n2))