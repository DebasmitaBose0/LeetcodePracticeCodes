from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()   # stores indices
        result = []
        
        for i in range(len(nums)):
            # Step 1: Remove out-of-window elements
            if dq and dq[0] == i - k:
                dq.popleft()
            
            # Step 2: Remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Step 3: Add current index
            dq.append(i)
            
            # Step 4: Append max to result
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result