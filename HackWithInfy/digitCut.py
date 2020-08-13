


def digitCut(num):
    l=[]
    s=""
    for ch in num:
        l.append(ch)
    low=0
    high=len(l)
    while low<=high:
        mid=(low+high)//2
        if l[mid]==l[mid+1]:
            del l[mid]
            del l[mid+1]
            print(*l)
            for i in l:
                s+=i
            return digitCut(s)
        else:
            return len(s)
    
    


num="888999"
print(digitCut(num))