class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # The maximum value of a single subarray is achieved by taking 
        # the max and min of the entire array.
        max_val = max(nums)
        min_val = min(nums)
        
        # Since we can repeat the same subarray k times, multiply by k
        return (max_val - min_val) * k