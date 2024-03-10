class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removed = 0
        i = 0
        l = len(nums)
        
        while i < l:
            if nums[i] == val:
                nums.pop(i)
                removed += 1
                i -= 1
                l -= 1
                nums.append('_')
            i += 1
        
        return len(nums) - removed