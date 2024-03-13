class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        
        if n == 1 or n == 2: return 1

        n -= 2
        T0 = 0
        T1 = 1
        T2 = 1
        Tn = None

        while n > 0:
            Tn = T0 + T1 + T2
            n -= 1

            T0 = T1
            T1 = T2
            T2 = Tn

        return Tn