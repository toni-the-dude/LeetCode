class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if len(nums) == 1: return True

        i = 1
        while i < len(nums) and nums[i - 1] <= nums[i]: i += 1
        if i == len(nums): return True

        i = 1
        while i < len(nums) and nums[i - 1] >= nums[i]: i += 1
        if i == len(nums): return True

        return False