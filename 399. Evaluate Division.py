import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. Build the graph
        # adj[node] = [(neighbor, weight), ...]
        adj = collections.defaultdict(list)
        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
            
        def bfs(src, target):
            # If variables don't exist in our equations, return -1.0
            if src not in adj or target not in adj:
                return -1.0
            
            # (current_node, current_product)
            queue = collections.deque([(src, 1.0)])
            visited = {src}
            
            while queue:
                curr, prod = queue.popleft()
                
                if curr == target:
                    return prod
                
                for neighbor, weight in adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, prod * weight))
            
            return -1.0
        
        # 2. Process each query
        return [bfs(q[0], q[1]) for q in queries]