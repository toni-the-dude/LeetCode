class Solution:
    def countAsterisks(self, s: str) -> int:
        
        output = 0
        within_pair = False

        for c in s:
            if c == '|': within_pair = not within_pair
            elif c == '*' and within_pair == False: output += 1

        return output