from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    s_all=input().split()
    dict_list=[]
    for s in s_all:
        arr=list(s)
        arr_dict=Counter(arr)
        dict_list.append(arr_dict)
    print()
    