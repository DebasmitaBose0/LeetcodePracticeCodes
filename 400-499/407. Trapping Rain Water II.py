import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # Add all boundary cells to the heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        water_trapped = 0
        # Directions for 4-connectivity (Up, Down, Left, Right)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while heap:
            height, r, c = heapq.heappop(heap)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    # If neighbor is lower than current boundary, it traps water
                    water_trapped += max(0, height - heightMap[nr][nc])
                    
                    # Push the neighbor into heap with the updated "boundary" height
                    heapq.heappush(heap, (max(heightMap[nr][nc], height), nr, nc))
                    visited[nr][nc] = True
                    
        return water_trapped