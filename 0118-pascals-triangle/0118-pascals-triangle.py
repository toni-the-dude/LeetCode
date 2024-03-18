class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal_triangle = [[1]]
        rows = 1
        
        while rows < numRows:
            
            pascal_triangle.append([1, 1])
            # print(pascal_triangle)
            for j in range(1, rows, 1):
                
                val1 = pascal_triangle[rows - 1][j - 1]
                val2 = pascal_triangle[rows - 1][j]
                # print(val1 + val2)
                pascal_triangle[rows].insert(j, val1 + val2)
            
            rows += 1
            
        return pascal_triangle
        