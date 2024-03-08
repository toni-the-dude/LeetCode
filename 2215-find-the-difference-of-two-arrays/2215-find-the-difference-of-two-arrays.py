class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_fr = {}
        nums2_fr = {}
        answer = [[],[]]
        
        for num in nums1:
            nums1_fr[num] = 0
                
        for num in nums2:
            nums2_fr[num] = 0
        
        for k in nums1_fr.keys():
            if k not in nums2_fr.keys():
                answer[0].append(k)
        
        for k in nums2_fr.keys():
            if k not in nums1_fr.keys():
                answer[1].append(k)        
    
        return answer