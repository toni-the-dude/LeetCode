class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()

        abs_min = 10**6

        for i in range(1, len(arr), 1):
            if arr[i] - arr[i - 1] < abs_min:
                abs_min = arr[i] - arr[i - 1]

        result = []

        for i in range(1, len(arr), 1):
            if arr[i] - arr[i - 1] == abs_min:
                result.append([arr[i - 1], arr[i]])

        return result