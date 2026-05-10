class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def solve(r, c, n):
            # Check if all values in the current n x n area are the same
            all_same = True
            for i in range(n):
                for j in range(n):
                    if grid[r][i] != grid[r+i][c+j]: # Conceptual check
                        # Real check: compare all to grid[r][c]
                        pass
            
            # Optimized uniformity check
            val = grid[r][c]
            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[i][j] != val:
                        all_same = False
                        break
                if not all_same: break
            
            if all_same:
                return Node(val == 1, True, None, None, None, None)
            
            # If not all same, divide into 4 quadrants
            half = n // 2
            top_left = solve(r, c, half)
            top_right = solve(r, c + half, half)
            bottom_left = solve(r + half, c, half)
            bottom_right = solve(r + half, c + half, half)
            
            return Node(True, False, top_left, top_right, bottom_left, bottom_right)

        return solve(0, 0, len(grid))