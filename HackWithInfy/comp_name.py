

def min_name(l):
    for i in range(97,123):
        for e in l:
            a=e.find(chr(i))
            if a!=-1:
                break
        break

    return i





t=int(input())
for i in range(t):
    l=[]
    N=int(input())
    for j in range(N):
        l.append(input())
    print(min_name(l))       