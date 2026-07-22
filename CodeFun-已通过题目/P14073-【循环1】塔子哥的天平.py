n,m=map(int,input().split())
n_com=list(map(int,input().split()))
n_sum=0
for i in n_com:
    n_sum+=i
m_com=list(map(int,input().split()))
m_sum=0
for i in m_com:
    m_sum+=i
if n_sum == m_sum:
    print("Equal")
else:
    print("Not Equal")
