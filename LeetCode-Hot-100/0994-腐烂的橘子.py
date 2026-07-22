class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        ans=0
        fresh=0
        init=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    init.append((i,j))
        while init and fresh:
            ans+=1
            tmp=init
            init=[]
            for apple in tmp:
                x,y=apple[0],apple[1]
                for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                    if 0<=i<m and 0<=j<n and grid[i][j]==1:
                        fresh-=1
                        grid[i][j]=2
                        init.append((i,j))
        return -1 if fresh else ans
