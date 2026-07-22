n=int(input())
arr=list(map(int,input().split()))
arr_map={}
ans=0
for j in range(len(arr)):
    dj=j+1-arr[j]
    if dj*-1 in arr_map:
        ans+=arr_map[dj*-1]
    if dj in arr_map:
        arr_map[dj]+=1
    else:
        arr_map[dj]=1
print(ans)
