#another pattern problem 2

arr=list("abcdefghijklmnopqrstuvwxyz")

n=int(input())
temp=[arr[i] for i in range(n)]

#upper half
for i in range(n-1):
  print("-".join(temp[:n-i-1:-1]+temp[n-i-1:]).rjust(4*n-3,"-"))
  temp1=temp[:n-i-2:-1]
  print("-".join(temp1+temp1[::-1]).rjust(4*n-3,"-"))

#mid
print("-".join(temp[::-1]+temp[1:]).rjust(4*n-3,"-"))

#lower half
for i in range(n-2,-1,-1):
  temp1=temp[:n-i-2:-1]
  print("-".join(temp1+temp1[::-1]).rjust(4*n-3,"-"))
  print("-".join(temp[:n-i-1:-1]+temp[n-i-1:]).rjust(4*n-3,"-"))
