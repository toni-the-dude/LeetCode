class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        nums.append(k)
        nums.sort()

        try:
            return nums.index(k)
        except ValueError:
            return len(nums) - 1