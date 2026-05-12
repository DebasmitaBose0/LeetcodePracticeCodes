import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        
        # Max number of bits for 10^18 is roughly 60
        # We start from the largest possible m to find the smallest k
        for m in range(int(math.log2(n)) + 1, 2, -1):
            # Estimate k as the (m-1)-th root of n
            k = int(n**(1 / (m - 1)))
            
            if k > 1:
                # Calculate the sum of the geometric series
                # n = (k^m - 1) / (k - 1)
                # Using pow(k, m) for large numbers
                if (pow(k, m) - 1) // (k - 1) == n:
                    return str(k)
        
        # Every n has a base n-1 where it is represented as "11"
        return str(n - 1)