#Satvik's sequence

a = int(input())
b = []
count=0
i=0
while count<=1000:
    i+=1
    if (i%3==0) or (i%10==3):
        continue
    else:
        b.append(i)
        count+=1

for i in range(a):
  c = int(input())
  print(b[c-1])
