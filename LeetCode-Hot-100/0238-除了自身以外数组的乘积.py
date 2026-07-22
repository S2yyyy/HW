class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]
        rev=[1]
        for i in range(len(nums)):
            pre.append(pre[-1]*nums[i])
        for i in range(len(nums)-1,-1,-1):
            rev.append(rev[-1]*nums[i])
        ans=[]
        for i in range(len(nums)):
            ans.append(pre[i]*rev[len(nums)-i-1])
        return ans
