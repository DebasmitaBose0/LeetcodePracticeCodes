import collections

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False
            
        # queue will store the indices that are reachable and can be used to jump further
        queue = collections.deque([0])
        
        # far keeps track of the maximum index we have explored or pushed to the queue so far
        # This prevents us from re-evaluating or re-adding duplicate indices.
        far = 0
        
        while queue:
            curr = queue.popleft()
            
            # The range of indices we can jump to from the current position
            start = max(curr + minJump, far + 1)
            end = min(curr + maxJump, n - 1)
            
            for j in range(start, end + 1):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    queue.append(j)
            
            # Update 'far' to ensure we never look back at indices we've already bounded
            far = max(far, curr + maxJump)
            
        return False