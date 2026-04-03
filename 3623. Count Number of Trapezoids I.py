class Solution:
    def countTrapezoids(self, points):
        from collections import Counter
        
        MOD = 10**9 + 7
        
        count = Counter(y for x, y in points)
        
        vals = []
        for c in count.values():
            if c >= 2:
                vals.append(c * (c - 1) // 2)
        
        total = sum(vals) % MOD
        
        total_sq = sum(v * v for v in vals) % MOD
        
        # (sum^2 - sum of squares) / 2
        ans = (total * total - total_sq) % MOD
        
        return (ans * pow(2, MOD - 2, MOD)) % MOD