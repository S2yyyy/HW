n,m=map(int,input().split())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
q=int(input())
for _ in range(q):
    x1,y1,x2,y2=map(int,input().split())
    max_num=0
    for i in range(x1-1,x2):
        for j in range(y1-1,y2):
            if matrix[i][j]>max_num:
                max_num=matrix[i][j]
    print(max_num)
