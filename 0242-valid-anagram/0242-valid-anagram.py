class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        freq = {}

        for char in s:
            
            try:
                freq[char] += 1
            except KeyError:
                freq[char] = 1

        for char in t:

            try:
                if freq[char] == 0: return False
                freq[char] -= 1
            except KeyError:
                return False

        return True