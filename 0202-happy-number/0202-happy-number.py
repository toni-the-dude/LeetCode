class Solution:
    def isHappy(self, n: int) -> bool:
        
        freq = {n: 1}

        while n > 1:
            aux = 0
            for digit in str(n):
                digit = int(digit)
                aux += digit * digit
            n = aux

            if n in freq.keys():
                return False
            else:
                freq[n] = 1
        
        if n == 1:
            return True

        return False
