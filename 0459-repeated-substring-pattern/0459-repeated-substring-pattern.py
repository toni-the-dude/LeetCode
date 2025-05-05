class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        l = len(s)
        d = 1

        while d <= l // 2:


            if (l // d) * s[:d] == s:
                return True

            d += 1 

        return False