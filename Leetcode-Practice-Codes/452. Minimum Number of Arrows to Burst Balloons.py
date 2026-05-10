class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # 1. Sort balloons by their end coordinates
        points.sort(key=lambda x: x[1])
        
        # 2. Initialize the first arrow at the end of the first balloon
        arrows = 1
        current_arrow_pos = points[0][1]
        
        # 3. Iterate through the rest of the balloons
        for i in range(1, len(points)):
            # If the current balloon starts AFTER the last arrow position
            if points[i][0] > current_arrow_pos:
                # We need a new arrow
                arrows += 1
                # Place the new arrow at the end of the current balloon
                current_arrow_pos = points[i][1]
        
        return arrows