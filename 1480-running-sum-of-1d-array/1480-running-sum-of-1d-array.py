class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        sum = nums[0]
        output = [nums[0]]

        for i in range(1, len(nums), 1):
            sum += nums[i]
            output.append(sum)

        return output