class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = 0
        sum = 0

        for num in gain:
            sum += num
            if sum > max: max = sum

        return max