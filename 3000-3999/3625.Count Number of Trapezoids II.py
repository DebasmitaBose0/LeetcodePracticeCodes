import math
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        slopes = defaultdict(list)
        
        for i in range(n):
            for j in range(i + 1, n):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                g = math.gcd(dx, dy)
                s_dy, s_dx = dy // g, dx // g
                if s_dx < 0 or (s_dx == 0 and s_dy < 0):
                    s_dy, s_dx = -s_dy, -s_dx
                slopes[(s_dy, s_dx)].append((i, j))
        
        ans = 0
        # mid -> dictionary of {slope: count_of_segments}
        midpoint_slope_counts = defaultdict(lambda: defaultdict(int))
        
        for slope, pairs in slopes.items():
            s_dy, s_dx = slope
            line_groups = defaultdict(int)
            
            for p1_idx, p2_idx in pairs:
                p1, p2 = points[p1_idx], points[p2_idx]
                C = s_dx * p1[1] - s_dy * p1[0]
                line_groups[C] += 1
                
                mid = (p1[0] + p2[0], p1[1] + p2[1])
                midpoint_slope_counts[mid][slope] += 1
            
            m = len(pairs)
            current_slope_combos = m * (m - 1) // 2
            for count in line_groups.values():
                current_slope_combos -= count * (count - 1) // 2
            ans += current_slope_combos

        # 2. Refined Parallelogram Calculation
        parallelograms = 0
        for mid, slope_map in midpoint_slope_counts.items():
            # Total pairs at this midpoint
            total_pairs_at_mid = sum(slope_map.values())
            # All combinations of pairs at this midpoint
            combos_at_mid = total_pairs_at_mid * (total_pairs_at_mid - 1) // 2
            
            # Subtract combinations where the segments have the same slope
            # (because these were already removed by the collinearity logic)
            for count in slope_map.values():
                combos_at_mid -= count * (count - 1) // 2
            
            parallelograms += combos_at_mid
                
        return ans - parallelograms