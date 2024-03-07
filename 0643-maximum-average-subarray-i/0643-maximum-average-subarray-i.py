class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        index = 0
        sum = 0

        while index < k:
            sum += nums[index]
            index += 1

        max = sum

        while index < len(nums):
            sum -= nums[index - k]
            sum += nums[index]
            index += 1
            if sum > max: max = sum

        return max / k