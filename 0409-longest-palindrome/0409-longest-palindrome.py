class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        letters = {}
        output = 0
        one_odd = False

        for l in s:
            try:
                letters[l] += 1
            except KeyError:
                letters[l] = 1

        for l in letters.keys():
            if letters[l] % 2 != 0:
                if one_odd == False:
                    output += letters[l]
                    one_odd = True
                else:
                    output += letters[l] - 1
            else:
                output += letters[l]

        return output