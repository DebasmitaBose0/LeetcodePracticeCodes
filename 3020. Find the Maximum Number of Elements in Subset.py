from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        
        # 1. Handle the special case of 1s
        if 1 in count:
            c1 = count[1]
            if c1 % 2 == 0:
                ans = c1 - 1
            else:
                ans = c1
        
        # 2. Check chains for x > 1
        for x in count:
            if x == 1:
                continue
                
            current_len = 0
            curr = x
            
            # Follow the chain of squares
            while curr in count:
                if count[curr] >= 2:
                    current_len += 2
                    curr = curr * curr
                else:
                    # It can only be the peak element
                    current_len += 1
                    break
            else:
                # If the loop ended because curr is not in count, 
                # the last element we processed needed to be the peak.
                # Since we added 2 for it, we must subtract 1 to make it a peak.
                current_len -= 1
                
            ans = max(ans, current_len)
            
        return ans