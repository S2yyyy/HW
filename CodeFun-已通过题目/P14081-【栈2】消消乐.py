arr=list(map(int,input().split()))
stack=[]
for i in range(len(arr)):
    if len(stack)>1:
        if stack[-1]==stack[-2] and stack[-1]==arr[i]:
            stack.pop()
            stack.pop()
            continue
        else:
            stack.append(arr[i])
    else:
        stack.append(arr[i])
if len(stack)>0:
    for i in stack:
        print(i,end=' ')
else:
    print('[]')
