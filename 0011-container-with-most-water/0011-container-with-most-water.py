class Solution:
    def maxArea(self, height: List[int]) -> int:

        begin = 0
        end = len(height) - 1
        max_water = 0

        while begin < end:
            smaller_height = min(height[end], height[begin])
            current_water = smaller_height * (end - begin)
            if current_water > max_water: max_water = current_water

            if height[begin] < height[end]: 
                begin += 1
            else: 
                end -= 1

        return max_water