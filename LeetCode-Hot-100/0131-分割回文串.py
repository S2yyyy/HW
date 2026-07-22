class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        def dfs(i, start,path):
            if i == n:
                ans.append(path)
                return
            if i < n-1:
                dfs(i+1,start,path)
            tmp = s[start:i+1]
            if tmp == tmp[::-1]:
                dfs(i+1,i+1,path+[tmp])
        dfs(0,0,[])
        return ans
