a=str(input())
b=str(input())
for i in range(len(a)+1):
    tar=a[:i]+b+a[i:]
    tar=list(tar)
    test=tar.copy()
    test.reverse()
    if "".join(test)=="".join(tar):
        print("YES")
        break
else:
    print("NO")
