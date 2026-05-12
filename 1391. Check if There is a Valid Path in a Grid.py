class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # This line must be indented once (4 spaces)
        n, m = len(grid), len(grid[0])
        seen = set([(0, 0)])
        
        # Mapping connections for each street type
        dirs = {
            1: [(0, -1), (0, 1)],  2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],  4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)], 6: [(0, 1), (-1, 0)]
        }

        def dfs(i, j):
            # This block must be indented twice (8 spaces)
            if i == n - 1 and j == m - 1:
                return True
            
            for di, dj in dirs[grid[i][j]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in seen:
                    # Validating the connection from the neighbor's side
                    if (-di, -dj) in dirs[grid[ni][nj]]:
                        seen.add((ni, nj))
                        if dfs(ni, nj):
                            return True
            return False

        return dfs(0, 0)