


def max_sum(arr):
    l=[-2,-3,4,-1,-2,1,5,-3]
    sT=sum(l)
    s=0
    for i in range(len(l)):
        s=s+l[i]
        sum_list.append(s)
    print(sum_list)
    m_s=max(sum_list)
    return m_s





arr=list(map(int,input("Enter array:").split()))
print(max_sum(arr))