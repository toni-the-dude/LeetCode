class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        length = len(nums)
        index = 0

        while index < length:
            if nums[index] == 0:
                nums.pop(index)
                zeroes += 1
                length -= 1
            else:
                index += 1

        while zeroes != 0:
            nums.append(0)
            zeroes -= 1
