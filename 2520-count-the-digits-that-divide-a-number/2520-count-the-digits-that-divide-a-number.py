class Solution:
    def countDigits(self, num: int) -> int:
        
        copy_of_num = num
        output = 0

        while copy_of_num != 0:
            if num % (copy_of_num % 10) == 0:
                output += 1
            copy_of_num //= 10

        return output