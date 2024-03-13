class Solution:
    def pivotInteger(self, n: int) -> int:
        
        i = n
        sum1 = n * (n + 1) / 2
        sum2 = n
        
        while i > 0:
            
            if sum1 == sum2:
                return i 
            
            sum2 += (i - 1)
            sum1 -= i          
            
            i -= 1
        
        return -1