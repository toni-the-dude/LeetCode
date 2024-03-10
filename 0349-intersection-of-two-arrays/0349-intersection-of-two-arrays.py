# Instructions are ambiguous to me. Might provide an inefficient solution.
# I was led to believe they wanted a sequence of numbers present in both arrays, at first
# Now, I believe they are asking for the numbers that are present in both arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fr = {}
        answer = []
        for n1 in nums1:
            if n1 not in fr.keys():
                fr[n1] = 0
        
        for n2 in nums2:
            if n2 in fr.keys():
                if fr[n2] == 0:
                    fr[n2] += 1
                    answer.append(n2)
                    
        return answer