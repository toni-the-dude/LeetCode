class Solution:
    def reverseDegree(self, s: str) -> int:
        
        rev_deg = 0

        for i in range(0, len(s), 1):
            rev_deg += (26 - (ord(s[i]) - 97)) * (i + 1)

        return rev_deg