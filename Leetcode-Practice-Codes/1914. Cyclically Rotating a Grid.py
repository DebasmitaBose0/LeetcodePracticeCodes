class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        
        for layer in range(layers):
            # Define boundaries for the current layer
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer
            
            # 1. Extract elements in counter-clockwise order
            elements = []
            for j in range(left, right): # Top row
                elements.append(grid[top][j])
            for i in range(top, bottom): # Right column
                elements.append(grid[i][right])
            for j in range(right, left, -1): # Bottom row
                elements.append(grid[bottom][j])
            for i in range(bottom, top, -1): # Left column
                elements.append(grid[i][left])
            
            # 2. Perform rotation
            # Counter-clockwise rotation by k means the new start 
            # of the array is at index (k % len(elements))
            num_elements = len(elements)
            real_k = k % num_elements
            rotated = elements[real_k:] + elements[:real_k]
            
            # 3. Put elements back into the grid
            idx = 0
            for j in range(left, right):
                grid[top][j] = rotated[idx]
                idx += 1
            for i in range(top, bottom):
                grid[i][right] = rotated[idx]
                idx += 1
            for j in range(right, left, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1
            for i in range(bottom, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1
                
        return grid