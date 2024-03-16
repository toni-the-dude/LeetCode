class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        count_keys = {0: 0}
        max_chain = count = 0
        
        for i in range(0, len(nums), 1):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
                
            if count in count_keys:
                max_chain = max(max_chain, i + 1 - count_keys[count])
            else:
                count_keys[count] = i + 1
                
        return max_chain