import sys
from collections import defaultdict

# Increase recursion depth for deep trees during DFS
sys.setrecursionlimit(200000)

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        n = len(edges) + 1
        MOD = 10**9 + 7
        
        # Step 1: Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Binary lifting table dimensions
        # LOGN = 18 is sufficient since 2^17 = 131072 > 10^5
        LOGN = 18
        up = [[0] * LOGN for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # Step 2: DFS to compute depths and immediate parents (2^0 ancestors)
        def dfs(node, parent, d):
            depth[node] = d
            up[node][0] = parent
            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs(neighbor, node, d + 1)
                    
        # Root the tree at node 1
        dfs(1, 1, 0)
        
        # Step 3: Populate the binary lifting (ancestor) table
        for j in range(1, LOGN):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j-1]][j-1]
                
        # Helper function to find the LCA of two nodes
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
                
            # Bring both nodes to the same depth
            diff = depth[u] - depth[v]
            for j in range(LOGN):
                if (diff >> j) & 1:
                    u = up[u][j]
                    
            if u == v:
                return u
                
            # Lift both nodes simultaneously right below their LCA
            for j in range(LOGN - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            return up[u][0]
            
        # Step 4: Process each query
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            lca = get_lca(u, v)
            # Calculate path length (number of edges)
            k = depth[u] + depth[v] - 2 * depth[lca]
            
            # Number of ways is 2^(k-1) % MOD
            ans.append(pow(2, k - 1, MOD))
            
        return ans