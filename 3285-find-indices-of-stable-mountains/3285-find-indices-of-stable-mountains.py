class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        
        output = []

        for i in range(1, len(height), 1):
            if height[i - 1] > threshold: output.append(i)

        return output