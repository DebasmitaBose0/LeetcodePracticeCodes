class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][cost] = max_score
        # Using -1 to represent unreachable states
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        
        # Initial position (0,0) - cost and score are 0 as per constraints
        dp[0][0][0] = 0
        
        for i in range(m):
            for j in range(n):
                # Skip the start cell since it's already initialized
                if i == 0 and j == 0:
                    continue
                
                # Cost and score for the current cell
                cell_val = grid[i][j]
                current_cost = 1 if cell_val > 0 else 0
                current_score = cell_val
                
                for c in range(current_cost, k + 1):
                    prev_max = -1
                    
                    # From top
                    if i > 0:
                        prev_max = max(prev_max, dp[i-1][j][c - current_cost])
                    # From left
                    if j > 0:
                        prev_max = max(prev_max, dp[i][j-1][c - current_cost])
                    
                    if prev_max != -1:
                        dp[i][j][c] = prev_max + current_score
        
        ans = max(dp[m-1][n-1])
        return ans