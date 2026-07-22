n=int(input())
arr=list(map(int,input().split()))
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    max=0
    for j in range(l-1,r):
        if arr[j]>max:
            max=arr[j]
    print(max)
    for j in range(l-1,r):
        if arr[j]==max:
            print(j+1,end=" ")
    print()
