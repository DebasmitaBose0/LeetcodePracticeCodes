import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # Calculate how many testing rounds we have
        tests = minutesToTest // minutesToDie
        
        # Each pig can provide (tests + 1) states of information
        # We need (tests + 1) ^ pigs >= buckets
        # Solving for pigs: pigs = ceil(log(buckets) / log(tests + 1))
        
        # We can use a simple loop or math.log
        pigs = 0
        while (tests + 1) ** pigs < buckets:
            pigs += 1
            
        return pigs