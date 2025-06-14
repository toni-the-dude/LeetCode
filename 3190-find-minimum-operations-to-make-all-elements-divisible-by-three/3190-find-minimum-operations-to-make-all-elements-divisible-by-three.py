class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        output = 0

        for num in nums:
            output += min(num % 3, 3 - num % 3)

        return output