from collections import deque
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Pair each number with its original index
        indexed_nums = sorted((val, i) for i, val in enumerate(nums))
        
        res = [0] * n
        
        # Groups will store collections of values and indices
        groups = []
        current_group_vals = deque()
        current_group_indices = deque()
        
        for val, idx in indexed_nums:
            if not current_group_vals or (val - current_group_vals[-1]) <= limit:
                current_group_vals.append(val)
                current_group_indices.append(idx)
            else:
                groups.append((current_group_vals, current_group_indices))
                current_group_vals = deque([val])
                current_group_indices = deque([idx])
                
        if current_group_vals:
            groups.append((current_group_vals, current_group_indices))
            
        # Place the sorted values back into their original sorted positions per group
        for vals, indices in groups:
            sorted_indices = sorted(indices)
            for i, idx in enumerate(sorted_indices):
                res[idx] = vals[i]
                
        return res