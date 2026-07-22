n,m,k=map(int,input().split())
l=int(m/n)
r=m
while l<=r:
    mid=int((l+r)/2)
    if k<=mid:
        left_total=(2*mid-k+1)*k/2
    else:
        left_total=(1+mid)*mid/2+k-mid
    if k+mid-1>=n:
        right_total=(n-k+1)*(2*mid+k-n)/2
    else:
        right_total=(1+mid)*mid/2+n-(k+mid-1)
    total=left_total+right_total-mid
    if total<=m:
        l=mid+1
    else:
        r=mid-1
print(r)
