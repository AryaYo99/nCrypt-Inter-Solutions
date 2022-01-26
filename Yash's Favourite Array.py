#Yash's Favourite Array
for t in range(int(input())):
    k=int(input())
    count=0
    while True:
        if k%2!=0:

            break
        else:
            k/=2
            count+=1
    print(count)
