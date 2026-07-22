arr=input().strip()
left=[]
right=[]
for i in arr:
    if i == "(":
        left.append(i)
    else:
        if len(left)==0:
            print("No")
            break
        left.remove(left[-1])
else:
    if len(left)==0:
        print("Yes")
    else:
        print("No")
