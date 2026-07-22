n=int(input())
n_map={}
arr=list(map(int,input().split()))
for i in range(n):
    if n_map.get(str(arr[i])) is None:
        n_map[str(arr[i])]=[i]
    else:
        n_map[str(arr[i])].append(i)
    if n_map.get(str(i)) is None:
        print(0,end=' ')
    else:
        print(len(n_map[str(i)]),end=' ')
