class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq = {}

        for c in s:
            try:
                freq[c] += 1
            except KeyError:
                freq[c] = 1
            
        for k, v in freq.items():
            if v == 1:
                return s.find(k)
        
        return -1