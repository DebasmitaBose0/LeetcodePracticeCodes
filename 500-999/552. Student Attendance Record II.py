class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # dp[count_A][consecutive_L]
        # We only need the previous day's data, so we use a 2D array
        dp = [[0, 0, 0], [0, 0, 0]]
        
        # Base case: Day 0 (empty string)
        dp[0][0] = 1 
        
        for i in range(n):
            new_dp = [[0, 0, 0], [0, 0, 0]]
            
            # j = number of 'A's (0 or 1)
            # k = consecutive 'L's at the end (0, 1, or 2)
            for j in range(2):
                for k in range(3):
                    if dp[j][k] == 0: continue
                    
                    # 1. Adding 'P'
                    new_dp[j][0] = (new_dp[j][0] + dp[j][k]) % MOD
                    
                    # 2. Adding 'A' (only if total 'A' < 1)
                    if j == 0:
                        new_dp[1][0] = (new_dp[1][0] + dp[j][k]) % MOD
                        
                    # 3. Adding 'L' (only if consecutive 'L' < 2)
                    if k < 2:
                        new_dp[j][k + 1] = (new_dp[j][k + 1] + dp[j][k]) % MOD
            
            dp = new_dp
            
        # Sum all valid states at day n
        return (sum(dp[0]) + sum(dp[1])) % MOD