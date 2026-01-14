class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows >= len(s) or numRows == 1: return s

        matrix = [[''] * len(s) for _ in range(numRows)]
        m_i = 0
        m_j = 0
        s_i = 0
        m_done = False
        # print(matrix)

        while s_i < len(s):
            while m_i < numRows: # Down
                # print(m_i, m_j, s_i)
                # print(matrix)
                matrix[m_i][m_j] = s[s_i]
                m_i += 1
                s_i += 1
                if s_i == len(s): 
                    m_done = True
                    break

            if m_done == True: break
            m_i = numRows - 2
            m_j += 1

            while m_i > 0: # Zig
                # print(m_i, m_j, s_i)
                # print(matrix)
                matrix[m_i][m_j] = s[s_i]
                m_i -= 1
                m_j += 1
                s_i += 1
                if s_i == len(s): 
                    m_done
                    break
            if m_done == True: break
        
        output_s = ""

        for i in range(numRows):
            for j in range(len(s)):
                if matrix[i][j] == '': continue
                output_s += matrix[i][j]

        return output_s