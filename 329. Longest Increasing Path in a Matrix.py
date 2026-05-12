class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        # Memoization table to store the longest path starting from each cell
        memo = [[0] * n for _ in range(m)]
        
        def dfs(r, c):
            # If already computed, return the cached result
            if memo[r][c] != 0:
                return memo[r][c]
            
            max_len = 1 # Minimum path length is the cell itself
            
            # Explore 4 directions: up, down, left, right
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and if the next cell is strictly greater
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))
            
            # Save to memo and return
            memo[r][c] = max_len
            return max_len
        
        # Run DFS from every cell to find the global maximum
        return max(dfs(r, c) for r in range(m) for c in range(n))