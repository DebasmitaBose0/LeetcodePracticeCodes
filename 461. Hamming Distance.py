class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 1. XOR x and y to get a number where bits are 1 only where they differ
        xor_result = x ^ y
        
        # 2. Count the number of set bits (1s) in the result
        # Python's bin().count('1') is a quick way to do this
        return bin(xor_result).count('1')