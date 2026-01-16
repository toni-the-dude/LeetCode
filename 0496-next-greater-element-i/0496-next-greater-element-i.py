class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums2HM = {value: index for index, value in enumerate(nums2)}
        output = []

        for num in nums1:
            toAdd = -1
            for i in range(nums2HM[num] + 1, len(nums2), 1):
                if nums2[i] > num: 
                    toAdd = nums2[i]
                    break
            output.append(toAdd)

        return output