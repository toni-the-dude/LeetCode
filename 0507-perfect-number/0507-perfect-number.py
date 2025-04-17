class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        if num <= 1: return False

        sum = 1
        div = 2

        while div * div <= num:

            if num % div == 0:
                sum += div

                if div != (num // div):
                    sum += (num // div)

            div += 1

        return sum == num