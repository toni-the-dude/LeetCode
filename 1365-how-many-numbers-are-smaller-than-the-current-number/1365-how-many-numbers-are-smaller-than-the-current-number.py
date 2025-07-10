class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        output = []

        for i in range(0, len(nums), 1):
            smaller = 0
            for j in range(0, len(nums), 1):
                if nums[j] < nums[i]:
                    smaller += 1
            output.append(smaller)

        return output