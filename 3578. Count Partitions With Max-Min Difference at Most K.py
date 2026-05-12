class Solution:
    def countPartitions(self, nums, k):
        from collections import deque
        
        MOD = 10**9 + 7
        n = len(nums)
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        prefix = [0] * (n + 1)
        prefix[0] = 1
        
        min_d = deque()
        max_d = deque()
        
        l = 0
        
        for r in range(n):
            # maintain min deque
            while min_d and nums[min_d[-1]] >= nums[r]:
                min_d.pop()
            min_d.append(r)
            
            # maintain max deque
            while max_d and nums[max_d[-1]] <= nums[r]:
                max_d.pop()
            max_d.append(r)
            
            # shrink window
            while nums[max_d[0]] - nums[min_d[0]] > k:
                if min_d[0] == l:
                    min_d.popleft()
                if max_d[0] == l:
                    max_d.popleft()
                l += 1
            
            # dp transition
            dp[r+1] = (prefix[r] - (prefix[l-1] if l > 0 else 0)) % MOD
            
            # update prefix
            prefix[r+1] = (prefix[r] + dp[r+1]) % MOD
        
        return dp[n]