from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        
        while queue:
            curr = queue.popleft()
            
            # Target found
            if arr[curr] == 0:
                return True
            
            # Skip if already visited
            if arr[curr] < 0:
                continue
                
            # Process neighbors (right and left jumps)
            for next_idx in (curr + arr[curr], curr - arr[curr]):
                if 0 <= next_idx < len(arr):
                    queue.append(next_idx)
            
            # Mark the current index as visited
            arr[curr] = -arr[curr]
            
        return False