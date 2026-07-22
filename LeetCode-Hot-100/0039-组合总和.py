class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def dfs(start,remain,path):
            if remain==0:
                ans.append(path)
                return
            for i in range(start,len(candidates)):
                if candidates[i]>remain:
                    return
                dfs(i,remain-candidates[i],path+[candidates[i]])
        dfs(0,target,[])
        return ans
