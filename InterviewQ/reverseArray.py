def rev_Array(arr):
    rev=[]
    for i in range(len(arr)-1,-1,-1):
        rev.append(arr[i])
    return rev





arr=list(map(int,input("Enter an Array:").split()))
print("Reverse  Array:",end='')
print(*rev_Array(arr))