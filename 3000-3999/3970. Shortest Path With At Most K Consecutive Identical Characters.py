import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list: u -> list of (v, w)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # Priority queue stores tuples of (current_distance, current_node, consecutive_count)
        pq = []
        
        # Distance table: dist[u][count] stores the min weight to reach node u with a given run length
        # Using a dictionary or 2D array. Since count ranges from 1 to k, a 2D array is efficient.
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        
        # Start at node 0. The first node has a run length of 1.
        initial_count = 1
        dist[0][initial_count] = 0
        heapq.heappush(pq, (0, 0, initial_count))
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            # If we reached the destination node, since Dijkstra explores by increasing weight,
            # the first time we pop node n-1, it is guaranteed to be the minimum total weight.
            if u == n - 1:
                return d
                
            if d > dist[u][count]:
                continue
                
            for v, w in adj[u]:
                # Determine the new consecutive identical character count
                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1
                    
                # If the consecutive count exceeds k, this path is invalid
                if next_count > k:
                    continue
                    
                new_dist = d + w
                if new_dist < dist[v][next_count]:
                    dist[v][next_count] = new_dist
                    heapq.heappush(pq, (new_dist, v, next_count))
                    
        return -1