#abhinav's integers
n=int(input())

arr=list(set(map(int,input().split())))

arr.sort()
store=[]
count=1
prev=arr[0]
for i in arr[1:]:

    if i==prev+1:
        count+=1
    else:
        store.append(count)
        count=1
    prev=i
store.append(count)

print(max(store))
