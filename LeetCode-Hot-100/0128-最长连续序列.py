class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length=0
        nums_set=set(nums)
        for i in nums_set:
            if i-1 not in nums_set:
                begin=i+1
                sub_max=1
                while begin in nums_set:
                    sub_max+=1
                    begin+=1
                if sub_max>max_length:
                    max_length=sub_max
        return max_length
