class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_list=list(s)
        s_dict={}
        begin=0
        ans=0
        for i in range(len(s_list)):
            if s_list[i] not in s_dict:
                s_dict[s_list[i]]=i
            else:
                while s_list[i] in s_dict:
                    s_dict.pop(s_list[begin])
                    begin+=1
                s_dict[s_list[i]]=i
            ans=max(ans,i-begin+1)
        return ans
