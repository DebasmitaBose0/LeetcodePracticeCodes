import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # Start from the integer part of the square root of area
        w = int(math.sqrt(area))
        
        # Decrement w until it becomes a divisor of area
        while area % w != 0:
            w -= 1
            
        # Once found, L is area / w
        return [area // w, w]