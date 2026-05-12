class Solution:
    def minimumFlips(self, n, edges, start, target):
        from collections import defaultdict
        
        g = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            g[u].append((v, i))
            g[v].append((u, i))
        
        need = [int(start[i]) ^ int(target[i]) for i in range(n)]
        res = []
        
        def dfs(u, parent):
            curr = need[u]
            
            for v, idx in g[u]:
                if v == parent:
                    continue
                
                child = dfs(v, u)
                
                if child == 1:
                    res.append(idx)
                    curr ^= 1
            
            return curr
        
        if dfs(0, -1) == 1:
            return [-1]
        
        return sorted(res)