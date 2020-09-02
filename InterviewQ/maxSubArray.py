


def max_sum(arr):
    l=[-2,1,-3,4,-1,2,1,-5,4]
    max_sum=l[0]
    current_sum=l[0]
    for i in range(1,len(l)):
        current_sum=l[i]
        max_sum=l[i]
        max_sum=max(max_sum,current_sum)
    return max_sum

        






arr=list(map(int,input("Enter array:").split()))
print(max_sum(arr))