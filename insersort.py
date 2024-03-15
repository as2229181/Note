import random
data=[]
for i in range(10):
    data.append(random.randint(1,100))
print(data)

def Insertsort(data):
    n=len(data)
    for i in range(n-1):
        key=data[i+1]
        j=i
        while j>=0 and key<data[j]:
            data[j+1]=data[j]
            j-=1
        data[j+1]=key
    return data
print(Insertsort(data))
         
