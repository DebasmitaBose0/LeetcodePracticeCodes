from itertools import accumulate
from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        pref = list(accumulate(stones))
        
        # Base case: taking all stones
        dp = pref[-1]
        
        # Iterate backwards from n - 2 down to 1
        for i in range(len(stones) - 2, 0, -1):
            dp = max(dp, pref[i] - dp)
            
        return dp