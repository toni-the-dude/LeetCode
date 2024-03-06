# https://leetcode.com/submissions/detail/1189969360/
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        if n == 1: return 1

        mid = n // 2
        left = 0
        right = n

        while True:
            # print("Mid:{0}".format(mid))

            g = guess(mid)

            if g == 0:
                return mid

            if g == -1: # Higher
                right = mid - 1
                mid = left + (right - left) // 2
                # print("Mid:{0}".format(mid))

            elif g == 1: # Lower
                left = mid + 1
                mid = left + (right - left) // 2
                # print("Mid:{0}".format(mid))


            elif right < left:
                return -1
