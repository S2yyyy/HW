import bisect
n,q=map(int,input().split())
arr=list(map(int,input().split()))
for _ in range(q):
    tar=int(input())
    left=bisect.bisect_left(arr,tar)-1
    right=bisect.bisect_right(arr,tar)
    left_num=arr[left] if left>0 else -1
    right_num=arr[right] if right<n else -1
    print(f"{left_num} {right_num}")