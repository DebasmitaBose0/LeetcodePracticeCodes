import math

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums)
        
        # dp[(g1, g2)] = count of disjoint subsequence pairs with GCDs g1 and g2
        # Use a hash map (dictionary) for space optimization and cleaner transitions
        dp = {(0, 0): 1}
        
        for num in nums:
            next_dp = dp.copy()
            
            for (g1, g2), count in dp.items():
                # Choice 1: Add num to the first subsequence
                new_g1 = math.gcd(g1, num)
                next_dp[(new_g1, g2)] = (next_dp.get((new_g1, g2), 0) + count) % MOD
                
                # Choice 2: Add num to the second subsequence
                new_g2 = math.gcd(g2, num)
                next_dp[(g1, new_g2)] = (next_dp.get((g1, new_g2), 0) + count) % MOD
                
            dp = next_dp
            
        # Sum all pairs where g1 == g2, excluding the empty-empty pair (0, 0)
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD
                
        return ans