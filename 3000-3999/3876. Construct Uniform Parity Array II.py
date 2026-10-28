class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odds = [x for x in nums1 if x % 2 == 1]
        evens = [x for x in nums1 if x % 2 == 0]
        
        min_odd = min(odds) if odds else float('inf')
        
        # Check if we can make everything even
        can_make_even = True
        for x in nums1:
            if x % 2 == 1:
                # Need to subtract an odd number to make it even, and result must be >= 1
                if min_odd == float('inf') or x - min_odd < 1:
                    can_make_even = False
                    break
        
        if can_make_even:
            return True
            
        # Check if we can make everything odd
        can_make_odd = True
        for x in nums1:
            if x % 2 == 0:
                # Need to subtract an odd number to make it odd, and result must be >= 1
                if min_odd == float('inf') or x - min_odd < 1:
                    can_make_odd = False
                    break
                    
        return can_make_odd