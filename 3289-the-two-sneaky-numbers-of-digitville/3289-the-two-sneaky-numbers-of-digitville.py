class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        freq = {}
        output = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] == 2: output.append(num)
            if len(output) == 2: return output

        return output