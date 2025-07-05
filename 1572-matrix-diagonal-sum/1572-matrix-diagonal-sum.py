class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        sum = 0
        n = len(mat)

        for i in range(0, n, 1):

            sum += mat[i][i] + mat[i][n - i - 1]

        if n % 2 == 1: return sum - mat[n // 2][n // 2]

        return sum