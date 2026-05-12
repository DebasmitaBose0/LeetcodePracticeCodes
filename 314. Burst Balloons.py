class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add virtual balloons with value 1 at both ends
        balloons = [1] + [b for b in nums if b > 0] + [1]
        n = len(balloons)
        
        # dp[i][j] will store the maximum coins obtained by bursting 
        # all balloons between index i and index j (exclusive)
        dp = [[0] * n for _ in range(n)]
        
        # k is the length of the range we are considering
        for k in range(2, n):
            # i is the left boundary
            for i in range(n - k):
                # j is the right boundary
                j = i + k
                # Try making every balloon 'm' between i and j the last to burst
                for m in range(i + 1, j):
                    # Coins = (coins from left sub-problem) + 
                    #         (coins from right sub-problem) + 
                    #         (coins from bursting balloon m)
                    coins = (dp[i][m] + dp[m][j] + 
                             balloons[i] * balloons[m] * balloons[j])
                    dp[i][j] = max(dp[i][j], coins)
                    
        return dp[0][n - 1]