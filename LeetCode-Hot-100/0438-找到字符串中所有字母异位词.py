class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        if len(s)<len(p):
            return ans
        box_s=[0]*26
        box_p=[0]*26
        for i in range(len(p)):
            box_s[ord(s[i])-97]+=1
            box_p[ord(p[i])-97]+=1
        if box_p==box_s:
            ans.append(0)
        for i in range(1,len(s)-len(p)+1):
            box_s[ord(s[i-1])-97]-=1
            box_s[ord(s[i+len(p)-1])-97]+=1
            if box_s==box_p:
                ans.append(i)
        return ans
