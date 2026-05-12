import math

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)
        
        # Track the minimum complexity seen so far from the left
        current_min = complexity[0]
        
        for i in range(1, n):
            # If the current computer has no computer to its left 
            # with a lower complexity, it can never be unlocked.
            if complexity[i] <= current_min:
                # We need to see if there is ANY j < i with lower complexity.
                # If the current_min is >= complexity[i], we must update 
                # current_min, but we also check if this computer i is unlockable.
                
                # Re-check: Does ANY j < i have complexity[j] < complexity[i]?
                # A simpler way: If complexity[i] is the new absolute minimum 
                # (or tied for it), it's impossible because index 0 must be the root.
                if complexity[i] <= current_min:
                    # If complexity[i] is <= the min of all previous, 
                    # there is no j < i such that complexity[j] < complexity[i].
                    return 0
            
            # Update min seen so far to keep the check efficient
            if complexity[i] < current_min:
                current_min = complexity[i]
                
        # If all computers are unlockable, Computer 0 must be first.
        # The other (n-1) elements can be in any order.
        return math.factorial(n - 1) % MOD