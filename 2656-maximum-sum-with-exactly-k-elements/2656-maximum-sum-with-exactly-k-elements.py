class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        m = max(nums)

        return (m + k - 1) * (m + k) // 2 - m * (m - 1) // 2