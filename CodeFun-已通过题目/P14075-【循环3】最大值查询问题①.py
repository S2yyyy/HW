n=int(input())
raw=list(map(int,input().split()))
arr=[]
for i in range(n):
    arr.append((raw[i],i))
arr.sort()
max_num=arr[-1][0]
print(max_num)
for i in range(n):
    if arr[i][0]==max_num:
        print(arr[i][1],end=" ")
