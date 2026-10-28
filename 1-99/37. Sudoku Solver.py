class Solution:
    def solveSudoku(self, board):
        
        def isValid(row, col, num):
            # Check row
            for j in range(9):
                if board[row][j] == num:
                    return False
            
            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False
            
            # Check 3x3 box
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            
            return True
        
        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        
                        for num in "123456789":
                            if isValid(i, j, num):
                                board[i][j] = num
                                
                                if backtrack():
                                    return True
                                
                                board[i][j] = "."  # undo
                        
                        return False
            
            return True
        
        backtrack()