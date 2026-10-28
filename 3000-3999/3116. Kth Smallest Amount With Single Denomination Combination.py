from math import gcd
from itertools import combinations
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def lcm(a: int, b: int) -> int:
            return (a * b) // gcd(a, b)
        
        # Precompute the LCM for all non-empty subsets
        n = len(coins)
        subset_lcms = []
        for r in range(1, n + 1):
            for combo in combinations(coins, r):
                cur_lcm = combo[0]
                for x in combo[1:]:
                    cur_lcm = lcm(cur_lcm, x)
                # Store (lcm_value, sign) where sign is +1 for odd size, -1 for even size
                sign = 1 if r % 2 == 1 else -1
                subset_lcms.append((cur_lcm, sign))
        
        def count_multiples(m: int) -> int:
            """Count distinct multiples of any coin <= m using PIE."""
            total = 0
            for l, sign in subset_lcms:
                total += sign * (m // l)
            return total

        # Binary search the range [min_coin, min_coin * k]
        left = 1
        right = min(coins) * k
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            if count_multiples(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans