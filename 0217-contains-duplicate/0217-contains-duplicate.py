class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dict = {}
        
        for num in nums:
            if num not in dict.keys():
                dict[num] = 0
            else:
                return True
            
        return False