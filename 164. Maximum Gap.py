class Solution:
    def maximumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        
        min_val = min(nums)
        max_val = max(nums)
        
        if min_val == max_val:
            return 0
        
        gap = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // gap + 1
        
        buckets = [[None, None] for _ in range(bucket_count)]
        
        for num in nums:
            idx = (num - min_val) // gap
            
            if buckets[idx][0] is None:
                buckets[idx][0] = buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)
        
        max_gap = 0
        prev_max = min_val
        
        for b in buckets:
            if b[0] is None:
                continue
            
            max_gap = max(max_gap, b[0] - prev_max)
            prev_max = b[1]
        
        return max_gap