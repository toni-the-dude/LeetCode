class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # (A) 65 - (Z) 90
        result = ""

        while columnNumber != 0:
            columnNumber -= 1
            result += chr(65 + (columnNumber % 26))
            columnNumber //= 26

        return result[::-1]