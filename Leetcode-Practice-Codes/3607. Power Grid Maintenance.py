from collections import defaultdict
import heapq

class Solution:
    def processQueries(self, c, connections, queries):
        
        # DSU
        parent = list(range(c + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa
        
        # Build components
        for u, v in connections:
            union(u, v)
        
        # Group nodes by component
        comp = defaultdict(list)
        for i in range(1, c + 1):
            root = find(i)
            comp[root].append(i)
        
        # For each component → min heap of online nodes
        heaps = {}
        online = [True] * (c + 1)
        
        for root, nodes in comp.items():
            heap = nodes[:]
            heapq.heapify(heap)
            heaps[root] = heap
        
        res = []
        
        for qtype, x in queries:
            root = find(x)
            
            if qtype == 1:
                if online[x]:
                    res.append(x)
                else:
                    heap = heaps[root]
                    
                    # Lazy removal
                    while heap and not online[heap[0]]:
                        heapq.heappop(heap)
                    
                    if heap:
                        res.append(heap[0])
                    else:
                        res.append(-1)
            
            else:  # qtype == 2
                online[x] = False
        
        return res