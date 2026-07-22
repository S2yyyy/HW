class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        max_s=0
        while i<j:
            sub_s=min(height[i],height[j])*(j-i)
            if sub_s>max_s:
                max_s=sub_s
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return max_s
