class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=set()
        n=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    m.add(i)
                    n.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in m or j in n:
                    matrix[i][j]=0
