class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        output = 0

        for i in range(0, len(nums) - 1, 1):
            for j in range(i + 1, len(nums), 1):
                if nums[i] == nums[j]:
                    output += 1

        return output