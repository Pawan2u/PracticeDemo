"""
11112
32222
43333
54444
65555
76666
"""



n=6
'''
for i in range(1,n+1):
    for j in range(1,n):
        print(i,end="")
        if 
    print()


for i in range(1,n+1,2):
    print(i,i,i,i,i+1)
    i+=1
    print(i+1,i,i,i,i)
'''
k=n
for i in range(n):
    for j in range(k):
        print("",end="")
    while j<=i:
        print("* ",end="")
        j+=1
    print()
    k-=1