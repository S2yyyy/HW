n=int(input())
ans=0
for i in range(1,n+1):
    sum=0
    i=int(i/10)
    while i>0:
        sum+=i
        i=int(i/10)
    if sum % 10 ==0:
        ans+=1
print(ans)
