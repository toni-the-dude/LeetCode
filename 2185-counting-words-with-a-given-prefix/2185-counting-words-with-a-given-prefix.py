class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        length_of_prefix = len(pref)
        output = 0

        for word in words:
            if word[:length_of_prefix] == pref: output += 1

        return output