class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        i_R = j_R = None
        attacking = 0
        # Locate rook
        for i in range(0, 8, 1):
            for j in range(0, 8, 1):
                if board[i][j] == 'R':
                    i_R = i
                    j_R = j
                    break
            if i_R != None: break
        # Right of rook
        for j in range(j_R + 1, 8, 1):
            
            if board[i_R][j] == 'B': break
            elif board[i_R][j] == 'p':
                attacking += 1
                break
        # Left of rook
        for j in range(j_R - 1, -1, -1):
            
            if board[i_R][j] == 'B': break
            elif board[i_R][j] == 'p':
                attacking += 1
                break
        # Above rook
        for i in range(i_R - 1, -1, -1):
            
            if board[i][j_R] == 'B': break
            elif board[i][j_R] == 'p':
                attacking += 1
                break
        # Below rook
        for i in range(i_R + 1, 8, 1):
            
            if board[i][j_R] == 'B': break
            elif board[i][j_R] == 'p':
                attacking += 1
                break
        
        return attacking