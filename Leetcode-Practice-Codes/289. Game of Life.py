class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        State transitions:
        0 : dead -> dead
        1 : live -> live
        2 : live -> dead (was 1, now 0)
        3 : dead -> live (was 0, now 1)
        """
        rows = len(board)
        cols = len(board[0])
        
        # 8 neighbors: horizontal, vertical, and diagonal
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    
                    # Boundary check + check if neighbor WAS alive (1 or 2)
                    # Parentheses ensure the boundary check protects both state checks
                    if 0 <= nr < rows and 0 <= nc < cols and (board[nr][nc] == 1 or board[nr][nc] == 2):
                        live_neighbors += 1
                
                # Rule 1 or 3: Any live cell with < 2 or > 3 live neighbors dies
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = 2 
                
                # Rule 4: Any dead cell with exactly 3 live neighbors becomes a live cell
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 3
        
        # Second pass: Finalize the transitions to the next state
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1