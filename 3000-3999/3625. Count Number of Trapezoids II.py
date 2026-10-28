class Solution:
    def countTrapezoids(self, points):
        from collections import defaultdict
        from math import gcd
        
        def C2(x):
            return x * (x - 1) // 2
        
        n = len(points)
        slope_map = defaultdict(list)
        
        # Step 1: all segments grouped by slope
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                dx = x2 - x1
                dy = y2 - y1
                
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                # normalize
                if dx < 0:
                    dx *= -1
                    dy *= -1
                elif dx == 0:
                    dy = 1
                
                slope_map[(dx, dy)].append((i, j))
        
        res = 0
        
        for segments in slope_map.values():
            k = len(segments)
            if k < 2:
                continue
            
            total = C2(k)
            
            # remove overlapping (same point)
            count = defaultdict(int)
            for u, v in segments:
                count[u] += 1
                count[v] += 1
            
            bad = 0
            for c in count.values():
                if c >= 2:
                    bad += C2(c)
            
            res += total - bad
        
        return res