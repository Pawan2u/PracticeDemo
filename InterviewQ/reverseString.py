def reverse(s):
    reverse=""
    for i in range(len(s)-1,-1,-1):
        reverse += s[i]
    return f'Reverse of {s} is {reverse}'

def reverse1(s):
    return s[::-1] 


s=input("Enter a string:")
print(reverse1(s))




