class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if nums == []:
            return []

        output = []

        begin = 0
        end = 0

        while end < len(nums) - 1:
            if nums[end] == nums[end + 1] - 1:
                end += 1
            elif begin == end:
                output.append(str(nums[begin]))
                begin += 1
                end += 1
            else:
                output.append(str(nums[begin]) + "->" + str(nums[end]))
                end += 1
                begin = end


        if begin == end:
            output.append(str(nums[-1]))
        else:
            output.append(str(nums[begin]) + "->" + str(nums[end]))

        return output