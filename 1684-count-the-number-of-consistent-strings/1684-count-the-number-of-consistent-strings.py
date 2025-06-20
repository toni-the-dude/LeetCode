class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        freq = {}
        output = 0

        for c in allowed:
            freq[c] = 1

        for word in words:
            consistent = True
            for c in word:
                if c not in freq:
                    consistent = False
                    break
            if consistent == True: output += 1
        
        return output