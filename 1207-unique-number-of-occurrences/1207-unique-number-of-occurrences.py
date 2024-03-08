class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}

        for value in arr:
            if value in occurrences:
                occurrences[value] += 1
            else:
                occurrences[value] = 1

        temp = occurrences.copy()
        for key, value in occurrences.items():
            temp.pop(key)
            if value in temp.values(): return False

        return True