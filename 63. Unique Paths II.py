class Solution:
    def uniquePathsWithObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        
        dp = [0] * n
        dp[0] = 1 if grid[0][0] == 0 else 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[j] = 0   # obstacle → no path
                elif j > 0:
                    dp[j] += dp[j-1]
        
        return dp[-1]