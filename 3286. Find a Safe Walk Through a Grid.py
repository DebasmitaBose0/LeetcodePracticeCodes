from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # min_cost[r][c] will store the minimum health lost to reach cell (r, c)
        min_cost = [[float('inf')] * n for _ in range(m)]
        
        # Initialize starting point
        min_cost[0][0] = grid[0][0]
        
        # Deque for 0-1 BFS: stores tuples of (row, col)
        queue = deque([(0, 0)])
        
        # Direction vectors for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            # If we reached the bottom-right corner, check if we have health left
            if r == m - 1 and c == n - 1:
                return (health - min_cost[r][c]) >= 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    weight = grid[nr][nc]
                    new_cost = min_cost[r][c] + weight
                    
                    # If we found a strictly better (cheaper) path to (nr, nc)
                    if new_cost < min_cost[nr][nc]:
                        min_cost[nr][nc] = new_cost
                        if weight == 0:
                            queue.appendleft((nr, nc)) # 0 weight -> Front
                        else:
                            queue.append((nr, nc))     # 1 weight -> Back
                            
        return False