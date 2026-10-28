from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components = 0
        
        # Step 2 & 3: Traverse each component via DFS
        for i in range(n):
            if not visited[i]:
                vertices_count = 0
                edges_count = 0
                
                # Stack for DFS traversal
                stack = [i]
                visited[i] = True
                
                while stack:
                    curr = stack.pop()
                    vertices_count += 1
                    edges_count += len(adj[curr])   # Add the degree of the current vertex
                    
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                
                # A component is complete if total degrees == V * (V - 1)
                if edges_count == vertices_count * (vertices_count - 1):
                    complete_components += 1
                    
        return complete_components