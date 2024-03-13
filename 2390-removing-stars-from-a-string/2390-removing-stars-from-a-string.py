class Solution:
    def removeStars(self, s: str) -> str:
        
        try:
            i = 0
            while True:
                if s[i] == '*':
                    j = i - 1
                    while j >= 0:
                        if s[j] != '*':
                            s = s[:j] + s[j + 1:i] + s[i + 1:]
                            i -= 2
                            break
                        j -= 1
                    if j == -1:
                        s = s[:i] + s[i + 1:]
                        i -= 1
                i += 1
        except IndexError:
            return s