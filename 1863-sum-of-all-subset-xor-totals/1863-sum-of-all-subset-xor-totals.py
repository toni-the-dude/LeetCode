import itertools

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        output = 0

        def xor_total(nums: List[int]):
            total = 0
            for num in nums:
                total = total ^ num 
            return total

        def all_subsets(nums: List[int]):
            subsets = []
            for r in range(len(nums) + 1):
                subsets.extend(itertools.combinations(nums, r))
            return subsets

        for s in all_subsets(nums):
            output += xor_total(s)

        return output