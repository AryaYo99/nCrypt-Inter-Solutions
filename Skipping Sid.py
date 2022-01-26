#skipping sid

x,k,d=map(int,input().split())

x=abs(x)


if d>0:
    do=x//d
    if do>=k:
        print(x-(k*d))
    else:
        
        if (k-do)%2==0:
            print(x%d)
        else:
            print(d-(x%d))
