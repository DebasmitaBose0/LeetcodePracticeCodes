import random
import bisect

class Solution:
    def __init__(self, w: List[int]):
        # Create a prefix sum array to represent the weight ranges
        self.prefix_sums = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sums.append(current_sum)
        self.total_sum = current_sum

    def pickIndex(self) -> int:
        # Pick a random number between 1 and the total weight
        target = random.randint(1, self.total_sum)
        
        # Binary search to find the index where the target fits
        # bisect_left returns the leftmost place in the sorted list 
        # to insert 'target' while maintaining order.
        return bisect.bisect_left(self.prefix_sums, target)