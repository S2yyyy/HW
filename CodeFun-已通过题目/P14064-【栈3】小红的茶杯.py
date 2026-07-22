x=list(map(int,input().split()))
stack=[]
for i in x:
    stack.append(i)
    change=True
    while True and change:
        if len(stack)>=2 and stack[-1]==stack[-2]:
            num_sum=stack[-1]*2
            stack.pop()
            stack.pop()
            stack.append(num_sum)
            continue
        y_sum=0
        j=len(stack)-2
        while y_sum<stack[-1] and j>=0:
            y_sum+=stack[j]
            j-=1
        if y_sum==stack[-1]:
            for _ in range(len(stack)-j-1):
                stack.pop()
            stack.append(2*y_sum)
            continue
        change=False
while len(stack)>0:
    print(stack.pop(),end=" ")

