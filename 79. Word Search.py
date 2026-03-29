class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        
        def dfs(i, j, k):
            # all characters matched
            if k == len(word):
                return True
            
            # boundary + mismatch check
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = "#"  # mark visited
            
            # explore 4 directions
            found = (dfs(i+1, j, k+1) or
                     dfs(i-1, j, k+1) or
                     dfs(i, j+1, k+1) or
                     dfs(i, j-1, k+1))
            
            board[i][j] = temp  # backtrack
            
            return found
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False