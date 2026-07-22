class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_pre=[0]
        for i in range(len(nums)):
            sum_pre.append(sum_pre[-1]+nums[i])
        sum_dict={}
        ans=0
        for i in range(len(sum_pre)):
            target=sum_pre[i]-k
            if target in sum_dict:
                ans+=len(sum_dict[target])  
            if sum_pre[i] in sum_dict:
                sum_dict[sum_pre[i]].append(i)
            else:
                sum_dict[sum_pre[i]]=[i]  
        return ans
