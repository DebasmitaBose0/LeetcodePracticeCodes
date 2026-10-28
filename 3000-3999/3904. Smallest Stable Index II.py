class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Precompute prefix maximums
        pref_max = [0] * n
        curr_max = -float('inf')
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            pref_max[i] = curr_max
            
        # Step 2: Precompute suffix minimums
        suff_min = [0] * n
        curr_min = float('inf')
        for i in range(n - 1, -1, -1):
            curr_min = min(curr_min, nums[i])
            suff_min[i] = curr_min
            
        # Step 3: Find the first stable index
        for i in range(n):
            if pref_max[i] - suff_min[i] <= k:
                return i
                
        return -1