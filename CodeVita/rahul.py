





n=int(input())
c=1
k=1
flag=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2==0:
            if i>=j:
                c+=1
                print(c,end='')
                flag=1
            else:
                print(" ",end="")
        else:
            if i>=j:
                if flag==1:
                    c+=1
                    print(c,end="")
                    flag=0
                print(c,end="")
                c=k
                k-=1
            else:
                print(" ",end='')
        

    print()