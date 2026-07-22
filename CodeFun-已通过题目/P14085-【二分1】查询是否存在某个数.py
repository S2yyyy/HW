n,m=map(int,input().split())
arr=list(map(int,input().split()))
for _ in range(m):
    tar=int(input())
    l=0
    r=n-1
    mid=int((l+r)/2)
    while tar!=arr[mid] and l<r:
        if tar<arr[mid]:
            r=mid
        else:
            l=mid+1
        mid=int((l+r)/2)
    if tar==arr[mid]:
        print('YES')
    else:
        print('NO')
