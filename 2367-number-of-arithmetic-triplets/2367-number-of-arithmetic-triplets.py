class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        dict = {num: 0 for num in nums}
        triplets = 0

        for k in dict.keys():
            if k + diff in dict and k + diff * 2 in dict: triplets += 1

        return triplets