class Solution:
    def customSortString(self, order: str, s: str) -> str:
        correct_order = {}
        permutation = ""
        wildcards = ""
        
        for i in range(0, len(order), 1):
            correct_order[order[i]] = i
            
        for char in s:
            if char not in correct_order:
                wildcards += char
            else:
                i = 0
                try:
                    while correct_order[char] > correct_order[permutation[i]]:
                        i += 1
                    permutation = permutation[:i] + char + permutation[i:] 
                except IndexError:
                    permutation += char
            
        if wildcards != "":
            return permutation + wildcards
        
        return permutation