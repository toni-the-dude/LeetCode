class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
        output = 0

        for i in range(0, len(s), 1):
            output += abs(i - t.find(s[i]))

        return output