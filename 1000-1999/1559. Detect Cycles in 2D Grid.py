class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        seen = set()

        def dfs(i, j, pi, pj, c):
            if (i, j) in seen:
                return True
            
            seen.add((i, j))
            
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                # 1. Stay within grid bounds
                # 2. Only move to cells with the same character 'c'
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == c:
                    # 3. Skip the cell we just came from (parent)
                    if (ni, nj) == (pi, pj):
                        continue
                    if dfs(ni, nj, i, j, c):
                        return True
            return False

        # Iterate through every cell to start a DFS if not visited
        for r in range(n):
            for l in range(m):
                if (r, l) not in seen:
                    # Start DFS: current (r,l), parent (-1,-1), target char grid[r][l]
                    if dfs(r, l, -1, -1, grid[r][l]):
                        return True
        return False