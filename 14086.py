n,q=map(int,input().split())
arr=list(map(int,input().split()))
for _ in range(q):
    l=0
    r=n-1
    mid=int((l+r)/2)
    tar=int(input())
    while l<r:
        mid=int((l+r)/2)
        if tar<=arr[mid]:
            r=mid-1
        else:
            l=mid
    if tar!=arr[mid]:
        print('-1 -1')
        continue
    else:
        print(mid+1,end=' ')
    l=0
    r=n-1
    mid=int((l+r)/2)
    while l<r:
        mid=int((l+r)/2)
        if tar<arr[mid]:
            r=mid
        else:
            l=mid+1
    print(mid+1)