class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        upper = len(s)
        lower = 0
        output = []

        for c in s:
            if c == "I":
                output.append(lower)
                lower += 1
            else:
                output.append(upper)
                upper -= 1
        output.append(lower)    
        return output