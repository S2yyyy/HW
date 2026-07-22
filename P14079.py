a=str(input())
b=str(input())
flag=0
for i in range(len(a)+1):
    tar=a[:i]+b+a[i:]
    tar=list(tar)
    test=tar.copy()
    test.reverse()
    if "".join(test)=="".join(tar):
        print("Yes")
        flag=1
if flag==0:
    print("No")