class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        output = []

        for num in range(left, right + 1, 1):

            selfd = True
            for digit in list(map(int, str(num))):

                if digit == 0 or num % digit != 0: 
                    selfd = False
                    break

            if selfd == True:
                output.append(num)
            
        return output
