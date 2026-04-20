class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2 or k == 0:
            return 0
        
        # States: 
        # 0: Empty (can start a new transaction)
        # 1: Holding Normal (bought, waiting to sell)
        # 2: Holding Short (sold, waiting to buy back)
        
        # Initialize DP with negative infinity
        # dp[k_remaining][state]
        dp = [[float('-inf')] * 3 for _ in range(k + 1)]
        
        # Base case: start with k transactions and 0 profit
        dp[k][0] = 0
        
        for price in prices:
            next_dp = [[float('-inf')] * 3 for _ in range(k + 1)]
            for j in range(k + 1):
                # State 0: Empty
                if dp[j][0] != float('-inf'):
                    # Option A: Stay empty
                    next_dp[j][0] = max(next_dp[j][0], dp[j][0])
                    # Option B: Start Normal (Buy)
                    next_dp[j][1] = max(next_dp[j][1], dp[j][0] - price)
                    # Option C: Start Short (Sell)
                    next_dp[j][2] = max(next_dp[j][2], dp[j][0] + price)
                
                # State 1: Holding Normal
                if dp[j][1] != float('-inf'):
                    # Option A: Keep holding
                    next_dp[j][1] = max(next_dp[j][1], dp[j][1])
                    # Option B: Sell Normal (Completes transaction)
                    if j > 0:
                        # Moves to state 0, but only for the NEXT day
                        next_dp[j-1][0] = max(next_dp[j-1][0], dp[j][1] + price)
                
                # State 2: Holding Short
                if dp[j][2] != float('-inf'):
                    # Option A: Keep holding short
                    next_dp[j][2] = max(next_dp[j][2], dp[j][2])
                    # Option B: Buy back (Completes transaction)
                    if j > 0:
                        # Moves to state 0, but only for the NEXT day
                        next_dp[j-1][0] = max(next_dp[j-1][0], dp[j][2] - price)
            
            dp = next_dp
            
        return max(dp[j][0] for j in range(k + 1))