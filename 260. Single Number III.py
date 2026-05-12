class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all numbers. 
        # The result (xor_all) will be (a ^ b) where a and b are the unique numbers.
        xor_all = 0
        for n in nums:
            xor_all ^= n
            
        # Step 2: Find a specific bit that is set in xor_all.
        # This bit must be different between a and b (one has 0, one has 1).
        # We use x & -x to get the rightmost set bit.
        diff_bit = xor_all & -xor_all
        
        # Step 3: Partition the numbers into two groups based on that bit.
        # XORing each group will reveal the two unique numbers.
        a = 0
        for n in nums:
            if n & diff_bit:
                a ^= n
        
        # Since a ^ b = xor_all, then b = xor_all ^ a
        return [a, xor_all ^ a]