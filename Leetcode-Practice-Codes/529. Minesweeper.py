class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click
        
        # Rule 1: Clicked on a mine
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        m, n = len(board), len(board[0])
        
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or board[i][j] != 'E':
                return
            
            # Count adjacent mines
            mine_count = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0: continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':
                        mine_count += 1
            
            if mine_count > 0:
                # Rule 3: Change to digit and stop recursion
                board[i][j] = str(mine_count)
            else:
                # Rule 2: Change to 'B' and recurse on neighbors
                board[i][j] = 'B'
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di == 0 and dj == 0: continue
                        dfs(i + di, j + dj)
        
        dfs(r, c)
        return board