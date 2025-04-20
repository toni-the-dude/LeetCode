class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        count = 0
        l = len(heights)

        expected = [heights[0]]

        for i in range(1, l, 1):

            skip = 0
            j = 0

            while heights[i] > expected[j]: 
                j += 1
                if j == len(expected):
                    expected.append(heights[i])
                    skip = 1
                    break

            if skip == 1:
                continue

            expected.insert(j, heights[i])


        for i in range(0, l, 1):
            print(expected[i], heights[i])
            if expected[i] != heights[i]: count += 1

        return count