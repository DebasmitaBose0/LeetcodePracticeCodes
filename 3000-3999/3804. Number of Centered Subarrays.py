class Solution:
    def centeredSubarrays(self, nums):
        n = len(nums)
        res = 0
        
        for i in range(n):
            s = 0
            seen = set()
            for j in range(i, n):
                s += nums[j]
                seen.add(nums[j])
                if s in seen:
                    res += 1
                    
        return res