import sys
import bisect
n,q=map(int,input().split())
arr=list(map(int,input().split()))
for _ in range(q):
    x=int(input())
    left=bisect.bisect_left(arr,x)
    if left==n or arr[left]!=x:
        print('-1 -1')
    else:
        right=bisect.bisect_right(arr,x)
        print(f"{left+1} {right}")
