from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        memo = [-1] * n
        
        def dfs(i: int) -> int:
            # If already calculated, return the cached result
            if memo[i] != -1:
                return memo[i]
            
            max_visited = 1  # Base case: standing at index i counts as 1 visited index
            
            # Look to the right
            for x in range(1, d + 1):
                j = i + x
                if j >= n or arr[j] >= arr[i]:
                    break  # Blocked by a wall or a taller/equal building
                max_visited = max(max_visited, 1 + dfs(j))
                
            # Look to the left
            for x in range(1, d + 1):
                j = i - x
                if j < 0 or arr[j] >= arr[i]:
                    break  # Blocked by a wall or a taller/equal building
                max_visited = max(max_visited, 1 + dfs(j))
                
            memo[i] = max_visited
            return memo[i]
        
        # Find the global maximum by trying to start from every single index
        return max(dfs(i) for i in range(n))