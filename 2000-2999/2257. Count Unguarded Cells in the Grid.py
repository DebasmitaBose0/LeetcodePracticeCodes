class Solution:
    def countUnguarded(self, m, n, guards, walls):
        grid = [[0] * n for _ in range(m)]
        
        # Mark guards
        for r, c in guards:
            grid[r][c] = -2
        
        # Mark walls
        for r, c in walls:
            grid[r][c] = -1
        
        # Directions: up, down, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == -1 or grid[nr][nc] == -2:
                        break
                    
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                    
                    nr += dr
                    nc += dc
        
        # Count unguarded cells
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        
        return count