class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        flag=False
        x,y=0,n-1
        while flag == False and x<m and y>=0:
            if matrix[x][y]==target:
                flag = True
            if matrix[x][y]>target:
                y-=1
            elif matrix[x][y]<target:
                x+=1
        return flag
