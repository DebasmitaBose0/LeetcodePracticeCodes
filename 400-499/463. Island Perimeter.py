class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Add 4 for the current land cell
                    perimeter += 4
                    
                    # If there's a land cell above, subtract the shared edges
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    
                    # If there's a land cell to the left, subtract the shared edges
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
                        
        return perimeter