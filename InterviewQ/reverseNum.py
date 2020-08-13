def reverse(n):
    temp=n
    reverse=0
    while n>0:
        rem=n%10
        reverse=(reverse*10)+rem
        n=n//10
    return f'Reverse of {temp} is {reverse}'




n=int(input("Enter a num:"))
print(reverse(n))