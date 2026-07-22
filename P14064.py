x=list(map(int,input().split()))
stack=[x[0]]
for i in range(1,len(x)):
    if x[i]==stack[-1]:
        sum=x[i]+stack.pop()
        stack.append(sum)
    else:
        stack.append(x[i])
    re_stack=stack[::-1]
    tar=0
    for j in range(1,len(re_stack)):
        tar+=re_stack[j]
        if tar>re_stack[0]:
            break
        elif tar ==re_stack[0]:
            for _ in range(j+1):
                stack.pop()
            stack.append(2*tar)
while len(stack)>0:
    print(stack.pop(),end=" ")

