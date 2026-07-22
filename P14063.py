n=int(input())
arr=list(map(int,input().split()))
oxarr=[]
for i in arr:
    weight=0
    while i>0:
        weight+=i % 16
        i=int(i/16)
    oxarr.append(weight)
local=[]
re_arr=oxarr[::-1]
max_num=0
max_local=-1
for i in range(len(arr)):
    if max_num<=re_arr[i]:
        local.append(-1)
        max_num=re_arr[i]
        max_local=i
    else:
        local.append(max_local)
local.reverse()
for i in local:
    print(len(arr)-i-1 if i != -1 else -1,end=' ')