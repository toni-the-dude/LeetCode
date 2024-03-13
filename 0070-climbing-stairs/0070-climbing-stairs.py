def fact(n):
    
    prod = 1
    
    for i in range(2, n + 1, 1):
        prod *= i
    
    return prod

def C(n, k):
    return fact(n) // (fact(n - k) * fact(k))

class Solution:
    def climbStairs(self, n: int) -> int:
        
        answer = 0
        k = 0
        
        while k <= n:
            answer += C(n, k)
            n -= 1
            k += 1
        
        return answer