"""
quick_sort

time complexity nlogn
every sca
"""


import random
data=[]
for i in range(10):
    data.append(random.randint(1,100))


def queicksort(data):
    n=len(data)
    if n<=1:
        return data
    left=[]
    right=[]
    pivot=data[0]
    for i in range(1,n):
        if data[i]<pivot:
            left.append(data[i])
        else:
            right.append(data[i])
    return queicksort(left)+[pivot]+queicksort(right)
print(queicksort(data))



def QuickSort(arr, start, end):
    if start < end:
        pivotIndex = partition(arr, start, end)
        QuickSort(arr, start, pivotIndex - 1)
        QuickSort(arr, pivotIndex + 1, end)
    return arr

def partition(arr, start, end):
    n = len(arr)
    pivot = arr[end]
    nextIndex = start
    for i in range(start,n-1):
        if arr[i] < pivot:
            arr[nextIndex],arr[i] = arr[i],arr[nextIndex]
            nextIndex += 1
    arr[nextIndex],arr[end] = arr[end],arr[nextIndex]
    return nextIndex
# print(QuickSort(data, 0 , len(data)-1))



# def quick_sort(arr, left, right):
#     if left >= right:
#         return
#     i = left
#     j = right
#     key = arr[left]

#     while i != j:
#         #  找右邊
#         while arr[j] > key and i < j:
#             j -= 1
#         #  找左邊
#         while arr[i] <= key and i < j:
#             i += 1
#         if i < j :
#             arr[i], arr[j] = arr[j], arr[i]
    
#     if i == j:
#         arr[left] = arr[i]
#         arr[i] = key
#     print(i)
#     quick_sort(arr, left, i-1)
#     quick_sort(arr, i+1, right)

    

# quick_sort(data, 0, len(data)-1)
# print(data)

