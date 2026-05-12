from collections import Counter
import math

class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        counts = Counter(balls).values()
        min_f = min(counts)
        
        # Try the largest possible 'k' (minimum group size) first
        for k in range(min_f, 0, -1):
            total_groups = 0
            possible = True
            
            for f in counts:
                # Calculate groups of size k+1
                num_groups = f // (k + 1)
                remainder = f % (k + 1)
                
                if remainder == 0:
                    total_groups += num_groups
                elif k - remainder <= num_groups:
                    # We can take (k - remainder) elements from existing groups 
                    # to make the remainder group size 'k'
                    total_groups += num_groups + 1
                else:
                    possible = False
                    break
            
            if possible:
                return total_groups
                
        return len(balls) # Fallback (shouldn't be reached)