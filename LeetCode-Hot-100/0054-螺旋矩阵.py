class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        direct=[[0,1],[1,0],[0,-1],[-1,0]]
        m=len(matrix)
        n=len(matrix[0])
        visit=[[0 for _ in range(n)] for _ in range(m)]
        di=0
        x,y=0,0
        for i in range(m*n):
            ans.append(matrix[x][y])
            visit[x][y]=1
            next_x,next_y=x+direct[di][0],y+direct[di][1]
            if next_x<0 or next_x>=m or next_y<0 or next_y>=n or visit[next_x][next_y]==1:
                di = (di+1)%4
            x+=direct[di][0]
            y+=direct[di][1]
        return ans
