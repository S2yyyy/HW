class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_pre=[0]
        min_sum=1000000
        max_sum=-1000000
        for i in range(len(nums)):
            sum_pre.append(sum_pre[-1]+nums[i])
            if min_sum>sum_pre[i]:
                min_sum=sum_pre[i]
            max_sum=max(max_sum,sum_pre[i+1]-min_sum)
        return max_sum
