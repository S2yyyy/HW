@cache
def dfs(remain, num):
    if remain == 0:
        return 0
    if num == 0:
        return inf
    if remain < num * num:
        return dfs(remain, num - 1)
    return min(dfs(remain, num - 1), dfs(remain - num * num, num) + 1)
        
class Solution:
    def numSquares(self, n: int) -> int:          
        return dfs(n, int(math.sqrt(n)))
