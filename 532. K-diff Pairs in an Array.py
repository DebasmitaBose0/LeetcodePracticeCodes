import collections

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # Step 1: Count the frequency of each number
        counts = collections.Counter(nums)
        pair_count = 0
        
        # Step 2: Iterate through the unique numbers in our map
        for x in counts:
            if k > 0:
                # If k > 0, check if the "target" number exists
                if x + k in counts:
                    pair_count += 1
            else:
                # If k = 0, we need at least two instances of the same number
                if counts[x] > 1:
                    pair_count += 1
                    
        return pair_count