class Solution:
    def numberOfPaths(self, grid, k):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        dp = [[[0]*k for _ in range(n)] for _ in range(m)]
        
        dp[0][0][grid[0][0] % k] = 1
        
        for i in range(m):
            for j in range(n):
                for r in range(k):
                    if i == 0 and j == 0:
                        continue
                    
                    val = grid[i][j]
                    
                    # from top
                    if i > 0:
                        prev = dp[i-1][j][r]
                        if prev:
                            dp[i][j][(r + val) % k] = (dp[i][j][(r + val) % k] + prev) % MOD
                    
                    # from left
                    if j > 0:
                        prev = dp[i][j-1][r]
                        if prev:
                            dp[i][j][(r + val) % k] = (dp[i][j][(r + val) % k] + prev) % MOD
        
        return dp[m-1][n-1][0]