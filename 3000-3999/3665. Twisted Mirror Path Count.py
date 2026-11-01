from ast import List
import sys

# Increase recursion depth just in case for large grids with deep recursive reflections
sys.setrecursionlimit(200000)

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        
        # memo[(r, c, dir)] -> final landing cell (nx, ny) or None
        memo = {}
        
        def find_exit(r, c, curr_dir):
            # If out of bounds, return None
            if not (0 <= r < m and 0 <= c < n):
                return None
            
            # If current cell is empty (0), this is our landing spot
            if grid[r][c] == 0:
                return (r, c)
            
            state = (r, c, curr_dir)
            if state in memo:
                return memo[state]
            
            # If it's a mirror (1), reflect based on entry direction
            if curr_dir == 0:  # entered moving right -> turns down
                nxt_r, nxt_c = r + 1, c
                nxt_dir = 1
            else:  # entered moving down -> turns right
                nxt_r, nxt_c = r, c + 1
                nxt_dir = 0
                
            memo[state] = find_exit(nxt_r, nxt_c, nxt_dir)
            return memo[state]

        # Precompute go transitions for all cells
        go = [[ [None, None] for _ in range(n) ] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # Move right initial step into (i, j+1), entering moving right (dir=0)
                go[i][j][0] = find_exit(i, j + 1, 0)
                # Move down initial step into (i+1, j), entering moving down (dir=1)
                go[i][j][1] = find_exit(i + 1, j, 1)

        # Standard DP traversal
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                val = dp[i][j]
                if val == 0:
                    continue
                
                # Propagate right move
                nxt_right = go[i][j][0]
                if nxt_right:
                    nr, nc = nxt_right
                    dp[nr][nc] = (dp[nr][nc] + val) % MOD
                
                # Propagate down move
                nxt_down = go[i][j][1]
                if nxt_down:
                    nr, nc = nxt_down
                    dp[nr][nc] = (dp[nr][nc] + val) % MOD
                    
        return dp[m - 1][n - 1]