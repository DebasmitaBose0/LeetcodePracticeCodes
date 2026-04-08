from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Base cases: if there are 0, 1, or 2 nodes, they are all MHT roots
        if n <= 2:
            return [i for i in range(n)]

        # Build adjacency list and track degrees of each node
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        # Find initial leaves (nodes with only one neighbor)
        leaves = deque([i for i in range(n) if len(adj[i]) == 1])

        # Trim leaves until 1 or 2 nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            
            # Remove current layer of leaves
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                # Find the only neighbor of this leaf
                neighbor = adj[leaf].pop()
                # Remove the leaf from the neighbor's set
                adj[neighbor].remove(leaf)
                
                # If neighbor becomes a leaf, add it to the next layer
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)
                    
        return list(leaves)