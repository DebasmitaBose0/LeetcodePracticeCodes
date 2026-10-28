class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 1. n must be positive
        # 2. n & (n - 1) == 0 checks if it's a power of two
        # 3. n & 0xaaaaaaaa == 0 ensures the bit is in an even-indexed position 
        #    (0, 2, 4...) which correspond to powers of 4.
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0