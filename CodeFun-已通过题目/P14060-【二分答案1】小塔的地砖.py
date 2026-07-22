t=int(input())
for _ in range(t):
    a,b,c,x,y=map(int,input().split())
    l=min([a,b,c])
    r=max([a,b,c])
    while l<=r:
        mid=int((l+r)/2)
        new_a=a
        new_b=b
        new_c=c
        if new_a>=mid:
            new_b+=int((new_a-mid)/x)
            new_a-=int((new_a-mid)/x)*x
        if new_b>=mid:
            new_c+=int((new_b-mid)/y)
            new_b-=int((new_b-mid)/y)*y
        if min([new_a,new_b,new_c])>=mid:
            l=mid+1
        else:
            r=mid-1
    print(r)
