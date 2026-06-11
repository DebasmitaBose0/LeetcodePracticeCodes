from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # Step 1: Build the adjacency list for the tree
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Step 2: Use BFS to find the maximum depth
        # Queue stores tuples of (current_node, current_depth)
        queue = deque([(1, 0)])
        visited = {1}
        max_depth = 0
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
        
        # Step 3: Compute 2^(max_depth - 1) % (10^9 + 7)
        MOD = 10**9 + 7
        
        # Handle edge case where max_depth is 0 (though constraints say n >= 2, so max_depth >= 1)
        if max_depth == 0:
            return 0
            
        return pow(2, max_depth - 1, MOD)