class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total_boomerangs = 0
        
        for p1 in points:
            # Hash map to store distance squared -> frequency
            distance_map = {}
            
            for p2 in points:
                # Calculate squared Euclidean distance
                dx = p1[0] - p2[0]
                dy = p1[1] - p2[1]
                dist_sq = dx*dx + dy*dy
                
                # Update frequency of this distance from the current anchor p1
                distance_map[dist_sq] = distance_map.get(dist_sq, 0) + 1
            
            # For each distance, if there are 'm' points, we can form m*(m-1) boomerangs
            for m in distance_map.values():
                total_boomerangs += m * (m - 1)
                
        return total_boomerangs