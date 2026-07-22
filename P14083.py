n,q=map(int,input().split())
arr=list(map(int,input().split()))
arr_map={}
for i in range(len(arr)):
    if arr_map.get(str(arr[i])) is None:
        arr_map[str(arr[i])]=[i]
    else:
        arr_map[str(arr[i])].append(i)
for _ in range(q):
    x,k=map(int,input().split())
    print(-1 if arr_map.get(str(x)) is None or len(arr_map[str(x)])<k else arr_map[str(x)][k-1]+1)