class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAPPING = ["","","abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        char_dict={str(i):MAPPING[i] for i in range(2,10)} 
        ans=[]
        def dfs(i,path):
            if i == len(digits):
                ans.append("".join(path))
                return
            for add_c in char_dict[digits[i]]:
                dfs(i+1,path+[add_c])
        dfs(0,[])
        return ans
