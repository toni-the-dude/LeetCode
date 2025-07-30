class Solution:
    def maxDepth(self, s: str) -> int:
        
        max = 0
        depth = 0

        for c in s:
            if c == "(": depth += 1
            elif c == ")": depth -= 1
            if depth > max: max = depth

        return max