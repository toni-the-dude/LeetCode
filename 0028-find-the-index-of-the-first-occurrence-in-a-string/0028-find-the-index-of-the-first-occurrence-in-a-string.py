class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) > len(haystack): return -1
        
        for c in range(0, len(haystack), 1):
            if haystack[c] == needle[0]:
                i = 1
                j = c + 1
                try:
                    while haystack[j] == needle[i]:
                        i += 1
                        j += 1
                except IndexError:
                    pass
                    
                if i == len(needle):
                    return c
                
        return -1