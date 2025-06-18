class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        i = n

        while i < 2 * n:
            nums.insert((i - n) * 2 + 1, nums.pop(i))
            i += 1

        return nums 
