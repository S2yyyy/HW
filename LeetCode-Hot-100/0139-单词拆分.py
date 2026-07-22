class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_length = max(map(len, wordDict))
        words = set(wordDict)
        @cache
        def dfs(remain):
            if remain == 0:
                return True
            for i in range(remain - 1, max(remain - max_length -1, -1), -1):
                if s[i:remain] in words and dfs(i):
                    return True
            return False
        return dfs(len(s))
