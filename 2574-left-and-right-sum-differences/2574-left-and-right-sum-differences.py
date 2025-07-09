class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        leftSum = []
        rightSum = []

        sum = 0

        for i in range(0, len(nums), 1):
            leftSum.append(sum)
            sum += nums[i]

        for i in range(0, len(nums), 1):
            sum -= nums[i]
            rightSum.append(sum)

        return [abs(leftSum[i] - rightSum[i]) for i in range(0, len(nums), 1)]