
"""Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent 
   elements if they are in wrong order
"""

def bubble_sort(arr):
    l=len(arr)
    for i in range(len(arr)-1):
        for j in range(l-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


arr=list(map(int,input("Enter array: ").split()))
print("Bubble Sort:",*bubble_sort(arr))
print("Hi")