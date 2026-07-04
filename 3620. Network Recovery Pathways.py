from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        g = [[] for _ in range(n)]
        indeg = [0] * n
        vals = []

        for u, v, w in edges:
            g[u].append((v, w))
            indeg[v] += 1
            vals.append(w)

        # Topological order
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)

        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        vals = sorted(set(vals))

        INF = 10 ** 30

        def ok(limit):
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in g[u]:
                    if w < limit:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

            return dist[n - 1] <= k

        if not ok(0):
            return -1

        lo, hi = 0, len(vals) - 1
        ans = vals[0]

        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(vals[mid]):
                ans = vals[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans