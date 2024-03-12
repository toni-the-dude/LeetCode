class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        
        if target <= nums[index]:
            return 0
        
        while index < len(nums):
            
            if target > nums[index]:
                try:
                    if target <= nums[index + 1]:
                        return index + 1
                except IndexError:
                    return index + 1
            
            index += 1
        
        return index