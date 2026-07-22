num=list(map(int,input().split()))
while len(num)>0:
    sum=0
    for i in num:
        sum+=i
    print(sum)
    try:
        num=list(map(int,input().split()))
    except:
        num=[]
