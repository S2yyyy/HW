from collections import Counter
n,q=map(int,input().split())
arr=list(map(int,input().split()))
count_map=Counter(arr)
for _ in range(q):
    print(count_map.get(int(input()),0))
