class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[0]*len(nums)
        def dfs(i,remains):
            if i == len(nums):
                ans.append(path.copy())
            for x in remains:
                path[i]=x
                dfs(i+1,remains-{x})
        dfs(0,set(nums))
        return ans
