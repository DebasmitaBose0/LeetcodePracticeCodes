import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        # Iterate through all possible values of a and b
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                # Calculate the potential c squared
                c_sq = a**2 + b**2
                
                # Check if c_sq is a perfect square
                c = int(math.sqrt(c_sq))
                
                # If c is an integer and within the limit n
                if c <= n and c*c == c_sq:
                    count += 1
                    
        return count