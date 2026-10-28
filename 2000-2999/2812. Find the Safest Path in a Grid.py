from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # If the start or end cell has a thief, the safeness factor is immediately 0
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        # Step 1: Multi-source BFS to calculate min distance to any thief for each cell
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                    
        # Step 2: Use a Max-Heap (Dijkstra) to find the path maximizing the minimum safeness
        # Python's heapq is a min-heap by default, so we store negative values to simulate a max-heap
        max_heap = [(-dist[0][0], 0, 0)]  # (negative_safeness, r, c)
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while max_heap:
            max_safe, r, c = heapq.heappop(max_heap)
            current_safe = -max_safe
            
            # If we reached the bottom-right corner, return the bottleneck safeness factor
            if r == n - 1 and c == n - 1:
                return current_safe
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # The safeness of the path to the next cell is throttled by the minimum encountered so far
                    next_safe = min(current_safe, dist[nr][nc])
                    heapq.heappush(max_heap, (-next_safe, nr, nc))
                    
        return 0