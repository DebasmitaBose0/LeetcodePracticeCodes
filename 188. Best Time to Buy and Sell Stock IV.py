from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        # If k is large enough, it's the unlimited transactions case
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                profit += max(0, prices[i] - prices[i-1])
            return profit
        
        # DP table: dp[i][j] = max profit with i transactions up to day j
        dp = [[0] * n for _ in range(k+1)]
        
        for i in range(1, k+1):
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i-1][j] - prices[j])
        
        return dp[k][n-1]