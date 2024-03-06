# https://leetcode.com/submissions/detail/1195830054/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        zeros = 0
        product_of_all = 1

        for number in nums:
            if number == 0: zeros += 1
            else: product_of_all *= number

        index = 0
        while index < len(nums):
            if nums[index] == 0 and zeros == 1:
                answer.append(product_of_all)
            elif zeros >= 1:
                answer.append(0)
            else:
                answer.append(product_of_all // nums[index])
            index += 1

        return answer
