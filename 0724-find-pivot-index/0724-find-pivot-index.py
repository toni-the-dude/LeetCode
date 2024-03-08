import numpy

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index = 0
        l_sum = numpy.sum(nums[:index])
        r_sum = numpy.sum(nums[index + 1:])

        if l_sum == r_sum: return index
        index += 1

        while index < len(nums):
            l_sum += nums[index - 1]
            r_sum -= nums[index]
            if l_sum == r_sum: return index
            index += 1

        return -1