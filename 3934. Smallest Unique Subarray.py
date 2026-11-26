from collections import Counter
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # Shift values by +1 so 0 never erases leading terms in polynomial hashing
        vals = [x + 1 for x in nums]

        base1, mod1 = 1315423911, (1 << 61) - 1
        base2, mod2 = 1000003, 1_000_000_007

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        for i in range(n):
            pow1[i + 1] = (pow1[i] * base1) % mod1
            pow2[i + 1] = (pow2[i] * base2) % mod2
            pref1[i + 1] = (pref1[i] * base1 + vals[i]) % mod1
            pref2[i + 1] = (pref2[i] * base2 + vals[i]) % mod2

        def has_unique_of_length(length: int) -> bool:
            counts = Counter()
            p1 = pow1[length]
            p2 = pow2[length]
            for start in range(n - length + 1):
                end = start + length
                h1 = (pref1[end] - pref1[start] * p1) % mod1
                h2 = (pref2[end] - pref2[start] * p2) % mod2
                counts[(h1, h2)] += 1
            return any(freq == 1 for freq in counts.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_of_length(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans