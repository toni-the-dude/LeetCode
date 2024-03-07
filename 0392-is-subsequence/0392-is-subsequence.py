class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s is "": return True

        if s[0] not in t: return False

        previous_find = t.find(s[0])

        for index in range(1, len(s)):
            if index != 0:
                current_find = t.find(s[index], previous_find + 1)
                if s[index] not in t or current_find < previous_find: return False
                previous_find = current_find
        
        return True