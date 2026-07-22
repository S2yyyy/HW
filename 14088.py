n=int(input())
arr=list(map(int,input().split()))
arr.sort()
c=int(input())
arr_dict={}
ans=0
for i in range(len(arr)):
    if arr[i] in arr_dict:
        arr_dict[arr[i]]+=1
    else:
        arr_dict[arr[i]]=1
    if c+arr[i] in arr_dict:
        ans+=arr_dict[c+arr[i]]
    if arr[i]-c in arr_dict:
        ans+=arr_dict[arr[i]-c]
print(ans)