class Solution:
    def countCollisions(self, directions: str) -> int:
        # remove safe cars
        directions = directions.lstrip('L').rstrip('R')
        
        # count moving cars that will collide
        return sum(1 for ch in directions if ch != 'S')