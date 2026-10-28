from collections import deque, defaultdict

class Solution:
    def specialNodes(self, n, edges, x, y, z):
        # build graph
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        # BFS function
        def bfs(start):
            dist = [-1] * n
            q = deque([start])
            dist[start] = 0
            
            while q:
                u = q.popleft()
                for v in g[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return dist
        
        dx = bfs(x)
        dy = bfs(y)
        dz = bfs(z)
        
        ans = 0
        
        for i in range(n):
            a, b, c = sorted([dx[i], dy[i], dz[i]])
            if a*a + b*b == c*c:
                ans += 1
        
        return ans