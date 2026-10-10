class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        total_k = k1 + k2
        
        # Calculate absolute differences
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_diff_sum = sum(diffs)
        
        # If total operations can cover all differences, the min sum is 0
        if total_diff_sum <= total_k:
            return 0
            
        # Frequency array for differences (max difference can be up to 10^5)
        max_val = max(diffs)
        count = [0] * (max_val + 2)
        for d in diffs:
            count[d] += 1
            
        # Greedily reduce from the largest difference down
        remaining_k = total_k
        for d in range(max_val, 0, -1):
            if count[d] > 0:
                # We want to reduce elements from `d` to `d - 1`
                # Take as many as we can afford with `remaining_k`
                take = min(remaining_k, count[d])
                count[d] -= take
                count[d - 1] += take
                remaining_k -= take
                
                if remaining_k == 0:
                    break
                    
        # Calculate the final sum of squared differences
        result = 0
        for d in range(max_val + 1):
            if count[d] > 0:
                result += count[d] * d * d
                
        return result