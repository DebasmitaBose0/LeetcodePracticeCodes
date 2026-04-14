import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # 1. Sort heaters to enable binary search
        heaters.sort()
        max_radius = 0
        
        for house in houses:
            # 2. Use binary search to find the insertion point of the house
            idx = bisect.bisect_left(heaters, house)
            
            # Distance to the heater on the right
            dist_right = heaters[idx] - house if idx < len(heaters) else float('inf')
            
            # Distance to the heater on the left
            dist_left = house - heaters[idx - 1] if idx > 0 else float('inf')
            
            # 3. The house is covered by the closest of the two
            current_house_min_dist = min(dist_left, dist_right)
            
            # 4. The global radius must be at least this large
            max_radius = max(max_radius, current_house_min_dist)
            
        return max_radius