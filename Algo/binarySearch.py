
""" Binary Search is applied when the array is in sorted array
     Complexity O(logn)
"""
#             RECURSION
def binarySearch(arr,low,high,num):

    if high>=low:
        mid=(low+high)//2

        if arr[mid]==num:
            return f'{num} is at {mid+1} position!'
        
        else:
            if arr[mid]<num:
                low=mid+1
                return binarySearch(arr,low,high,num)
        
            else:
                high=mid-1
                return binarySearch(arr,low,high,num)
    
    else:
        return f'{num} is not found!'


arr=list(map(int,input("Enter array:").split()))
low=0
high=len(arr)-1
arr.sort()
print("Your Sorted array:",*arr)
num=int(input("Enter Element:"))
print(binarySearch(arr,low,high,num))