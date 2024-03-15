import random
data=[]
for i in range(10):
    data.append(random.randint(1,100))
print(data)

def merge_sort(data):
    if len(data) > 1:
        left_arr=data[:len(data)//2]
        right_arr=data[len(data)//2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                data[k] = left_arr[i]
                i += 1
            else:
                data[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            data[k] = left_arr[i]
            i += 1
            k += 1 
        while j < len(right_arr):
            data[k] = right_arr[j]
            j += 1
            k +=1       

def vertify_sort(list):
    n=len(list)
    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and vertify_sort(list[1:])


merge_sort(data)
print(data)