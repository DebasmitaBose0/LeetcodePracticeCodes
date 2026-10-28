class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Optimization: The length of any valid path from (0, 0) to (m-1, n-1) is m + n - 1.
        # A valid parentheses string must have an even length.
        if (m + n - 1) % 2 != 0:
            return False
        
        # We can use memoization to store visited states: (r, c, balance)
        # To avoid TLE, we use@cache or a visited set.
        from functools import cache
        
        @cache
        def dfs(r: int, c: int, balance: int) -> bool:
            # Update balance based on the current cell
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1
            
            # If at any point close brackets exceed open brackets, it's invalid
            if balance < 0:
                return False
            
            # If we reached the bottom-right cell
            if r == m - 1 and c == n - 1:
                return balance == 0
            
            # Move down or right
            res = False
            if r + 1 < m:
                res = res or dfs(r + 1, c, balance)
            if c + 1 < n:
                res = res or dfs(r, c + 1, balance)
                
            return res
        
        return dfs(0, 0, 0)