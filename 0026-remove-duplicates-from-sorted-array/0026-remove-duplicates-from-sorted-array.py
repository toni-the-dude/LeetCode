class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 0
        while i < len(nums):
            # print(nums[i])
            # print(nums)
            if nums[i] == '_': 
                break
            try:
                if nums[i + 1] == nums[i]:
                    nums.pop(i)
                    nums.append('_')
                    i -= 1
                else:
                    k += 1
            except IndexError:
                k += 1
                break
            i += 1
        # print(nums)
        # print(k)
        return k