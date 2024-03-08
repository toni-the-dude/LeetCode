class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        fr = [0 for i in range(0, 101, 1)]
        max_fr = 0
        count = 0
        
        for num in nums:
            fr[num] += 1
            if fr[num] > max_fr:
                max_fr = fr[num]
                count = fr[num]
            elif fr[num] == max_fr:
                count += fr[num]
                
        return count