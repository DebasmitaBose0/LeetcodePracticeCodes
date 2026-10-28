import collections
from ast import List
class Solution:

    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        adj = collections.defaultdict(list)
        for u, v in invocations:
            adj[u].append(v)

        # Step 1: Find all suspicious methods using BFS/DFS starting from k
        suspicious = set()
        queue = collections.deque([k])
        suspicious.add(k)

        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)

        # Step 2: Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        # Step 3: Remove suspicious methods and return remaining
        return [i for i in range(n) if i not in suspicious]