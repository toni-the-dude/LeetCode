class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        sum = 0
        l = len(nums)

        for num in nums:

            sum += num

        return l * (l + 1) // 2 - sum