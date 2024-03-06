class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max = -1
        output = []

        for number in candies:
            if number > max: max = number

        for number in candies:
            if number + extraCandies >= max:
                output.append(True)
            else: output.append(False)

        return output