class Solution:
    def maxSubarraySum(self, nums, k):
        import math
        
        prefix = 0
        ans = -math.inf
        
        # store min prefix for each mod
        min_prefix = [math.inf] * k
        min_prefix[0] = 0  # prefix before start
        
        for i, num in enumerate(nums):
            prefix += num
            mod = (i + 1) % k
            
            if min_prefix[mod] != math.inf:
                ans = max(ans, prefix - min_prefix[mod])
            
            min_prefix[mod] = min(min_prefix[mod], prefix)
        
        return ans