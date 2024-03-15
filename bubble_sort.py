
import random
data=[]
for i in range(10):
    data.append(random.randint(1,100))

print(data)


def bubble_sort(arr):
    n = len(arr)
    sort = False
    while sort is False:
        sort = True
        #  There is no number after the last number 
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                sort = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr
    

print(bubble_sort(data))