class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        fr = {}
        n = len(grid[0])
        pairs = 0
        
        for i in range(0, n, 1):
            row = tuple(grid[i:][0])
            
            if row not in fr:
                fr[row] = 1
            else:
                fr[row] += 1
        
        for i in range(0, n, 1):
            temp = []
            
            for j in range(0, n, 1):
                temp.append(grid[j][i])
                
            temp = tuple(temp)
            
            if temp in fr:
                print("match")
                pairs += fr[temp]
            
        
        return pairs