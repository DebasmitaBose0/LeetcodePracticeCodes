from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        
        # Step 1: Map each value to all its indices
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        # Step 2: Initialize BFS structures
        queue = deque([(0, 0)]) # Each element is a tuple: (current_index, current_steps)
        visited = {0}
        
        while queue:
            idx, steps = queue.popleft()
            
            # If we've reached the last index, return the steps taken
            if idx == n - 1:
                return steps
                
            # Step 3: Gather all potential next moves
            next_indices = [idx - 1, idx + 1]
            
            # Add the teleportation jumps if the value hasn't been cleared yet
            if arr[idx] in graph:
                next_indices.extend(graph[arr[idx]])
                # CRITICAL: Clear the entry so we don't look through this list again
                del graph[arr[idx]]
                
            # Step 4: Validate and push valid moves to the queue
            for next_idx in next_indices:
                if 0 <= next_idx < n and next_idx not in visited:
                    visited.add(next_idx)
                    queue.append((next_idx, steps + 1))
                    
        return -1