class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0
        majority = None

        for el in nums:

            if count == 0: majority = el
            
            if el == majority:
                count += 1
            else:
                count -= 1

        return majority
