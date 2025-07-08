class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        dict = {}
        max_v = max_c = ''
        max_v_nr = max_c_nr = 0

        for c in s:
            dict[c] = dict.get(c, 0) + 1

            if c in "aeiou":
                if dict[c] > max_v_nr:
                    max_v_nr = dict[c]
                    max_v = c
            else:
                if dict[c] > max_c_nr:
                    max_c_nr = dict[c]
                    max_c = c                    

        return max_v_nr + max_c_nr