class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0 or x == 1:
            return x
        
        index = 2
        
        while index * index <= x:
            index += 1
            
        return index - 1