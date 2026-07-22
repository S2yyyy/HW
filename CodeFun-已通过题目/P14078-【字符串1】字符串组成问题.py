a=str(input())
b=str(input())
loop=int(len(b)/len(a))
acc=""
for i in range(loop):
    acc+=a
if acc==b:
    print("Yes")
else:
    print("No")
