class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = nums[0]

        for index in range(1, len(nums)):
            answer = answer ^ nums[index] 

        return answer