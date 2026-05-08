class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Check if n is positive and if it divides the largest power of 3
        # 3^19 = 1162261467
        return n > 0 and 1162261467 % n == 0