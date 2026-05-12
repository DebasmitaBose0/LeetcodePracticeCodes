from functools import lru_cache
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)
        
        # Map each character to its positions in the ring
        pos = defaultdict(list)
        for i, char in enumerate(ring):
            pos[char].append(i)
            
        @lru_cache(None)
        def solve(k_idx, r_idx):
            # Base case: all characters in key are spelled
            if k_idx == m:
                return 0
            
            res = float('inf')
            # Try every position of the current key character in the ring
            for next_r_idx in pos[key[k_idx]]:
                # Calculate clockwise and anti-clockwise distance
                diff = abs(r_idx - next_r_idx)
                dist = min(diff, n - diff)
                
                # Recursive call + dist + 1 (for the button press)
                res = min(res, dist + 1 + solve(k_idx + 1, next_r_idx))
            
            return res
            
        return solve(0, 0)