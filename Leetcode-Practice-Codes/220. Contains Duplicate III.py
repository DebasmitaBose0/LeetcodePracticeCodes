class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False
        
        buckets = {}
        size = valueDiff + 1
        
        for i, num in enumerate(nums):
            bucket_id = num // size
            
            # same bucket
            if bucket_id in buckets:
                return True
            
            # neighbor buckets
            if (bucket_id - 1 in buckets and 
                abs(num - buckets[bucket_id - 1]) <= valueDiff):
                return True
            
            if (bucket_id + 1 in buckets and 
                abs(num - buckets[bucket_id + 1]) <= valueDiff):
                return True
            
            buckets[bucket_id] = num
            
            # maintain window size
            if i >= indexDiff:
                old_bucket = nums[i - indexDiff] // size
                del buckets[old_bucket]
        
        return False