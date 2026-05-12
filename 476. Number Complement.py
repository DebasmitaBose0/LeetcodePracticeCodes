class Solution:
    def findComplement(self, num: int) -> int:
        # 1. Calculate the number of bits in num
        # bit_length() is a built-in method in Python for integers
        bit_len = num.bit_length()
        
        # 2. Create a mask of all 1s with the same length
        # Example: if bit_len is 3, mask is (1 << 3) - 1 = 8 - 1 = 7 (111)
        mask = (1 << bit_len) - 1
        
        # 3. XOR the number with the mask to flip the bits
        return num ^ mask