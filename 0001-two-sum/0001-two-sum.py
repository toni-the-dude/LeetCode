class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fr = {}
        
        i = 0
        
        for i in range(0, len(nums), 1):
            if nums[i] not in fr:
                fr[nums[i]] = i
            if (target - nums[i]) in fr.keys():
                if (target - nums[i]) == (nums[i]):
                    if i != fr[target - nums[i]]:
                        return [i, fr[target-nums[i]]]
                else: return [i, fr[target-nums[i]]]
            
        return [0, 0]