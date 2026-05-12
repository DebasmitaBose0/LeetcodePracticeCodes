class Solution:
    def minSubarray(self, nums, p):
        total = sum(nums)
        rem = total % p
        
        if rem == 0:
            return 0
        
        prefix = 0
        res = len(nums)
        seen = {0: -1}  # prefix_mod → index
        
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            
            target = (prefix - rem + p) % p
            
            if target in seen:
                res = min(res, i - seen[target])
            
            seen[prefix] = i
        
        return res if res < len(nums) else -1