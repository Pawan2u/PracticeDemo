def fib(n):
    f_list=[0,1]
    if n==1:
        return f_list[0]
    elif n==2:
        return f_list[1]
    else:
        for i in range(2,n):
            f_list.append(f_list[i-2]+f_list[i-1])
    return f_list


n=int(input("Enter the term:"))
print(*fib(n))