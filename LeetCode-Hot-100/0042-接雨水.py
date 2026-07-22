class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        height_max=max(height)
        while left<right and height[left]==0:
            left+=1
        while left<right and height[right]==0:
            right-=1
        ans=0
        sub_sum=0
        while left<right:
            i=left+1
            while i<=right and height[i]<height[left]:
                sub_sum+=height[i]
                i+=1
            if i-left>1 and i!=right+1:
                ans+=min(height[left],height[i])*(i-left-1)-sub_sum
                sub_sum=0
            if i==right+1:
                break
            left=i
        sub_sum=0
        if left<right:
            while left<right:
                i=right-1
                while i>=left and height[i]<height[right]:
                    sub_sum+=height[i]
                    i-=1
                if right-i>1 :
                    ans+=min(height[right],height[i])*(right-i-1)-sub_sum
                    sub_sum=0
                if i==left:
                    break
                right=i
        return ans
