class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        # Base case: for n = 1, there is exactly 1 way to end at each value
        # dp[0][x] -> ending with value x, next move must be DOWN (0)
        # dp[1][x] -> ending with value x, next move must be UP (1)
        # Note: mapping values [l, r] to 0-indexed [0, m-1]
        dp0 = [1] * m
        dp1 = [1] * m
        
        for i in range(2, n + 1):
            next_dp0 = [0] * m
            next_dp1 = [0] * m
            
            # Prefix sums of the previous step to optimize transitions
            # pref0[x] = sum(dp0[0...x-1])
            # pref1[x] = sum(dp1[0...x-1])
            pref0 = [0] * (m + 1)
            pref1 = [0] * (m + 1)
            
            for x in range(m):
                pref0[x + 1] = (pref0[x] + dp0[x]) % MOD
                pref1[x + 1] = (pref1[x] + dp1[x]) % MOD
                
            for y in range(m):
                # 1. To move DOWN to y (next move will be UP -> next_dp1), 
                # the previous element x must be strictly greater than y (x > y).
                # Total ways = sum(dp0[x]) for x from y+1 to m-1
                # matches: pref0[m] - pref0[y+1]
                next_dp1[y] = (pref0[m] - pref0[y + 1]) % MOD
                
                # 2. To move UP to y (next move will be DOWN -> next_dp0), 
                # the previous element x must be strictly less than y (x < y).
                # Total ways = sum(dp1[x]) for x from 0 to y-1
                # matches: pref1[y]
                next_dp0[y] = pref1[y]
                
            dp0 = next_dp0
            dp1 = next_dp1
            
        # The total valid configurations of length n is the sum of all possibilities
        return (sum(dp0) + sum(dp1)) % MOD