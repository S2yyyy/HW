class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]
        for i in prices:
            if i < min_price:
                min_price = i
            ans = max(ans, i - min_price)
        return ans
