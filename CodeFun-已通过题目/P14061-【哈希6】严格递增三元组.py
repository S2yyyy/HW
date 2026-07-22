n=int(input())
arr=list(map(int,input().split()))
front=[]
after=[]
arr_dict={}
re_arr_dict={}
for i in range(n):
    if arr[i] in arr_dict:
        arr_dict[arr[i]].append(i)
    else:
        arr_dict[arr[i]]=[i]
    if arr_dict.get(arr[i]+1) is None:
        front.append(0)
    else:
        front.append(len(arr_dict[arr[i]+1]))
re_arr=arr[::-1]
for i in range(n):
    if re_arr[i] in re_arr_dict:
        re_arr_dict[re_arr[i]].append(i)
    else:
        re_arr_dict[re_arr[i]]=[i]
    if re_arr_dict.get(re_arr[i]+1) is None:
        after.append(0)
    else:
        after.append(len(re_arr_dict[re_arr[i]+1]))
after=after[::-1]
ans=0
for i in range(n):
    ans+=front[i]*after[i]
print(ans)
