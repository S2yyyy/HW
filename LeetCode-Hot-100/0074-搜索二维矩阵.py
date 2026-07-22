class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n-1
        for i in range(m+n):
            if x >= m or y < 0:
                return False
            if matrix[x][y] < target:
                x += 1
            elif matrix[x][y] > target:
                y -= 1
            else:
                return True
        return False
