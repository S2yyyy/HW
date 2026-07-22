class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0 
        max_right = 0
        cur = 0
        for i in range(len(nums) - 1):
            max_right = max(max_right, i+nums[i])
            if i == cur :
                ans += 1
                cur = max_right
        return ans
