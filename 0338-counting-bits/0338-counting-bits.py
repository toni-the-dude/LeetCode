class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        answer = [0] * (n + 1)

        for number in range(1, n + 1):
            answer[number] = answer[number // 2] + number % 2
            
        return answer
        