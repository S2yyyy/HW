n,d,k=map(int,input().split())
w=list(map(int,input().split()))
t=list(map(int,input().split()))
ans=[]
for i in range(n):
    com=list(map(int,input().split()))
    score=0
    for j in range(d):
        score+=(com[j+1]-t[j])*(com[j+1]-t[j])*w[j]
    ans.append((score,com[0]))

ans.sort()
print(" ".join(map(str,[x[1] for x in ans[:k]])))