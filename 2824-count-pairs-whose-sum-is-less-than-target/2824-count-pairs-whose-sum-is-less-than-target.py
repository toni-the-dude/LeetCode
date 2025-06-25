class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        output = 0

        for i in range(0, len(nums) - 1, 1):
            for j in range(i + 1, len(nums), 1):
                if nums[i] + nums[j] < target: output += 1

        return output