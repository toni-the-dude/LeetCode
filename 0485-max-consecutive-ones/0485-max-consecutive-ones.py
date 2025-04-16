class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max = 0
        current = 0

        for nr in nums:
            if nr == 1: current += 1
            else: current = 0
            if current > max: max = current

        return max