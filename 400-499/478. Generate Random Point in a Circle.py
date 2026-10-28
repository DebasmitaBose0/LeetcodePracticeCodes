import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # Generate a random angle between 0 and 2*pi
        theta = random.uniform(0, 2 * math.pi)
        
        # Use sqrt(random) to ensure uniform distribution over the area
        # Formula: r = R * sqrt(U) where U is uniform [0, 1]
        r = self.radius * math.sqrt(random.uniform(0, 1))
        
        # Convert polar coordinates (r, theta) to Cartesian (x, y)
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        
        return [x, y]