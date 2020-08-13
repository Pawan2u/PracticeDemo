def prime(limit):
    l=[2]
    count=1
    for i in range(2,limit+1):
        for j in range(2,i):
            if i%j==0:
                break
            elif i==j+1:
                count+=1
                l.append(i)
    print(count)
    return l

limit=int(input("Enter Limit:"))
print(*prime(limit))

