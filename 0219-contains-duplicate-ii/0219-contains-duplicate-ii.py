class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        freq = {}

        for i in range(0, len(nums), 1):
            if freq.get(nums[i]) != None:
                if abs(i - freq[nums[i]]) <= k:
                    return True
            freq[nums[i]] = i
            
        return False