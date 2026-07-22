class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_right = 0
        cur = 0
        while cur <= max_right and cur < len(nums):
            max_right = max(max_right, cur + nums[cur])
            cur += 1
        if cur == len(nums):
            return True
        return False
