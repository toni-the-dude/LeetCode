class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0
        i = 0
        while i < len(s):
            char = s[i]
            if char == "I" and (i + 1) != len(s):
                if s[i + 1] == "V":
                    number += 4
                    i += 1
                elif s[i + 1] == "X":
                    number += 9
                    i += 1
                else:
                    number += romans[char]
            elif char == "X" and (i + 1) != len(s):
                if s[i + 1] == "L":
                    number += 40
                    i += 1
                elif s[i + 1] == "C":
                    number += 90
                    i += 1
                else:
                    number += romans[char]
            elif char == "C" and (i + 1) != len(s):
                if s[i + 1] == "D":
                    number += 400
                    i += 1
                elif s[i + 1] == "M":
                    number += 900
                    i += 1
                else:
                    number += romans[char]
            else: number += romans[char]
            i += 1
                
        return number