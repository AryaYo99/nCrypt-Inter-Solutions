#president's order

n,m,q=map(int, input().split())

arr=[i for i in range(1,n+1)]
my=list(map(int, input().split()))
mem=list(map(int, input().split()))
count=0

arr=list(set(arr).difference(set(my)))


for j in mem:
    temp=arr.copy()

    for i in range(len(temp)):
        if temp[i]%j==0:
            arr.remove(temp[i])
            count+=1
print(count)
