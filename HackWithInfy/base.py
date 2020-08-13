

def decToN(n,num):

    mydict={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',23:'',24:'N',25:'O'}
    result=""

    while(num>0):
        rem = num % n
        num=int(num/n)

        if rem >=10:
            result += mydict[rem]
        else:
            result += str(rem)
    
    return result[::-1]


n=int(input("Enter n:"))
num=int(input("Enter num:"))
print(decToN(n,num))