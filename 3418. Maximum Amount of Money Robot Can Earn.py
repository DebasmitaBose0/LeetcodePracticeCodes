class Solution:
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        dp = [[[-10**18]*3 for _ in range(n)] for _ in range(m)]
        
        if coins[0][0] >= 0:
            dp[0][0][0] = coins[0][0]
        else:
            dp[0][0][0] = coins[0][0]
            dp[0][0][1] = 0
        
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if dp[i][j][k] == -10**18:
                        continue
                    
                    for ni, nj in [(i+1, j), (i, j+1)]:
                        if ni < m and nj < n:
                            val = coins[ni][nj]
                            
                            if val >= 0:
                                dp[ni][nj][k] = max(dp[ni][nj][k], dp[i][j][k] + val)
                            else:
                                dp[ni][nj][k] = max(dp[ni][nj][k], dp[i][j][k] + val)
                                if k < 2:
                                    dp[ni][nj][k+1] = max(dp[ni][nj][k+1], dp[i][j][k])
        
        return max(dp[m-1][n-1])