class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        prefix = ""
        prev_c = ""
        try:
            while True:
                prev_c = strs[0][index]
                for string in strs[1:]:
                    if prev_c != string[index]:
                        return prefix
                prefix += prev_c
                index += 1
        finally:
            return prefix