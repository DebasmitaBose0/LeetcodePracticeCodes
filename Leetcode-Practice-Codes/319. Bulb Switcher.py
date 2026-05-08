import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # The number of perfect squares up to n is the integer part of sqrt(n)
        return isqrt(n)