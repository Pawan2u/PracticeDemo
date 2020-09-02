"""
    There is no logic in Linear Seach.
      Complexity o(n)
"""


def linearSearch(arr,num):
    for i in range(len(arr)):
        if arr[i]==num:
            return f'{arr[i]} is at position {i+1}';
        
    return f'{num} is not found!'






arr=list(map(int,input("Enter array:").split()))
num=int(input("Enter Element:"))
print(linearSearch(arr,num))