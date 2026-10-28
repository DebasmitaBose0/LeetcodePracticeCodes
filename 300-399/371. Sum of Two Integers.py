class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to get 32-bit representation
        mask = 0xFFFFFFFF
        
        while b & mask > 0:
            # Carry: bits that are 1 in both a and b
            carry = (a & b) << 1
            # Sum: bits that are different in a and b
            a = a ^ b
            b = carry
        
        # If b is greater than 0, it means there's an overflow into the sign bit
        return (a & mask) if b > 0 else a