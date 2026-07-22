class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        @cache
        def dfs(lens, remain):
            if remain == 0:
                return 0
            if lens < 0:
                return inf
            if coins[lens] > remain:
                return dfs(lens - 1, remain)
            return min(dfs(lens - 1, remain), dfs(lens, remain - coins[lens]) + 1)
        ans = dfs(len(coins) - 1, amount)
        return ans if ans != inf else -1
