
from ast import List
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # Sort the asteroids in non-decreasing order
        asteroids.sort()
        
        # Greedily collide with the smallest available asteroid
        for asteroid in asteroids:
            if mass >= asteroid:
                mass += asteroid
            else:
                # If the planet can't destroy this asteroid, it's impossible
                return False
                
        return True