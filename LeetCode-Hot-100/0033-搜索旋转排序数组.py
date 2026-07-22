class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[-1] > nums[0]:
            target_index = bisect.bisect_left(nums,target)
            if target_index < len(nums) and nums[target_index] == target:
                return target_index
            return -1 
        else:
            if nums[-1] < target < nums[0]:
                return -1
            def findMin(nums):
                left, right = 0, len(nums)-1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] <= nums[-1]:
                        right = mid - 1
                    else:
                        left = mid + 1
                return left
            min_index = findMin(nums)
            if target == nums[min_index]:
                return min_index
            elif target <= nums[-1]:
                target_index = bisect.bisect_left(nums[min_index:],target)
                if target_index + min_index < len(nums) and nums[target_index + min_index] == target:
                    return target_index + min_index
                return -1
            else:
                target_index = bisect.bisect_left(nums[:min_index],target)
                if target_index < min_index and nums[target_index] == target:
                    return target_index
                return -1 
