from collections import Counter
t=int(input())
char='abcdefghijklmnopqrstuvwxyz'
char=list(char)
for _ in range(t):
    n=int(input())
    s_all=input().split()
    dict_list=[]
    for s in s_all:
        arr=list(s)
        arr_dict=Counter(arr)
        dict_list.append(arr_dict)
    out=0
    for i in char:
        flag=1
        min_print=10000000
        for j in dict_list:
            if i in j:
                min_print=min(min_print,j[i])
            else:
                flag=0
        if flag==1:
            print(i*min_print,end='')
            out=1
    if out==0:
        print(-1)
    else:
        print()
    
