class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = right = 0
        current_str = {}
        max_l = current_l = 0

        for c in s:
            try:
                current_str[c] += 1
            except KeyError:
                current_str[c] = 1
            if current_str[c] == 2:
                while current_str[c] == 2:
                    current_str[s[left]] -= 1 
                    left += 1
                    current_l -= 1
            current_l += 1
            if current_l > max_l: max_l = current_l

        return max_l
            