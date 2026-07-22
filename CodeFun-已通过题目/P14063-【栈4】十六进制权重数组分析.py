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
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if oxarr[j]>oxarr[i]:
            local.append(j)
            break
    if len(local)>i:
        continue
    local.append(-1)
for i in local:
    print(i,end=' ')
