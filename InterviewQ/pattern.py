

def pattern(n):
    i_=1
    j_=n-2
    for i in range(n):
        for j in range(n):
            if(i==0 or i==n-1):
                print("*",end="")
            elif(i==i_ and j==j_):
                print("*",end="")
                i_+=1
                j_-=1
            else:
                print(" ",end="")

        print()

def pattern2(n):
    for i in range(n):
        for j in range(n):
            if:
                print(i+1)

n=int(input("Enter a num:"))
pattern(n)