import random
import bisect

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix_sums = []
        total_points = 0
        
        for a, b, x, y in rects:
            # Number of integer points in this rectangle: (width + 1) * (height + 1)
            num_points = (x - a + 1) * (y - b + 1)
            total_points += num_points
            self.prefix_sums.append(total_points)

    def pick(self) -> List[int]:
        # Pick a random point index from 1 to total_points
        target = random.randint(1, self.prefix_sums[-1])
        
        # Binary search to find which rectangle this point index belongs to
        idx = bisect.bisect_left(self.prefix_sums, target)
        
        # Get the chosen rectangle coordinates
        a, b, x, y = self.rects[idx]
        
        # Calculate how many points were in previous rectangles
        prev_points = self.prefix_sums[idx-1] if idx > 0 else 0
        
        # Determine the relative point index within the chosen rectangle
        relative_idx = target - prev_points - 1
        
        # Convert the relative index back into (u, v) coordinates
        width = x - a + 1
        u = a + (relative_idx % width)
        v = b + (relative_idx // width)
        
        return [u, v]