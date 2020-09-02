
''' 
    Sort the array repeatedly finding minimum element from unsorted part
    complexity = O(n2)
Step 1 − Set MIN to location 0
Step 2 − Search the minimum element in the list
Step 3 − Swap with value at location MIN
Step 4 − Increment MIN to point to next element
Step 5 − Repeat until list is sorted

'''


def selection_sort(arr,length):
    count=0
    for i in range(length):
        min_index=i
        for j in range(i+1,length):
            if arr[min_index] > arr[j]:
                min_index=j
            count+=1
        arr[i],arr[min_index]=arr[min_index],arr[i]
        
    return arr,count   
    




arr=list(map(int,input("Enter array:").split()))
length=len(arr)
print("Sorted Array is:",end='')
print(*selection_sort(arr,length))