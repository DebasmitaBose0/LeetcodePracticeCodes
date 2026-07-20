from typing import List
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        # Flatten 2D grid to 1D
        flat = [val for row in grid for val in row]
        
        # Effective shifts needed
        k %= len(flat)
        
        # Perform rotation
        flat = flat[-k:] + flat[:-k]
        
        # Reconstruct 2D grid
        return [flat[i * n : (i + 1) * n] for i in range(m)]