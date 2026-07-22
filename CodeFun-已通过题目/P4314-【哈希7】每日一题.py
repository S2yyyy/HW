n=int(input())
s=list(input())
s_dict={}
sum=0
for i in range(n):
    if s[i] in s_dict:
        sum+=i-s_dict[s[i]]
        s_dict[s[i]]+=1
    else:
        sum+=i
        s_dict[s[i]]=1
    print(sum)
