class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        
        averages = []

        for i in range(len(nums), len(nums) // 2, -1):
            mn = nums.pop(nums.index(min(nums)))
            mx = nums.pop(nums.index(max(nums)))
            averages.append((mn + mx) / 2)

        return min(averages)
