from typing import List
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        # Find indices of min and max elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Ensure i is the smaller index and j is the larger index
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        
        # Scenario 1: Delete both from the front (reach index j + 1)
        del_front = j + 1
        
        # Scenario 2: Delete both from the back (reach from index i to end)
        del_back = n - i
        
        # Scenario 3: Delete one from the front and one from the back
        del_both = (i + 1) + (n - j)
        
        return min(del_front, del_back, del_both)