class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        sorted_points_by_x = [p[0] for p in points]
        sorted_points_by_x.sort()
        max_width = 0

        for i in range(0, len(sorted_points_by_x) - 1, 1):
            if sorted_points_by_x[i + 1] - sorted_points_by_x[i] > max_width: 
                max_width = sorted_points_by_x[i + 1] - sorted_points_by_x[i]

        return max_width
