from collections import defaultdict, deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Build the adjacency list graph
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Step 2: BFS traversal starting from city 1
        min_score = float('inf')
        queue = deque([1])
        visited = {1}
        
        while queue:
            node = queue.popleft()
            
            for neighbor, weight in graph[node]:
                # Track the minimum road weight seen in this connected component
                min_score = min(min_score, weight)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score