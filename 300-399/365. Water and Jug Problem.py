import math

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # If the target is more than the combined capacity, it's impossible
        if target > x + y:
            return False
        
        # If target is 0, we can always achieve it (both jugs empty)
        if target == 0:
            return True
        
        # The target must be a multiple of the GCD of x and y
        return target % math.gcd(x, y) == 0