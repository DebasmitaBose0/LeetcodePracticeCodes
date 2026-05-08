class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0
        
        # Iterate from the 30th bit down to the 0th bit
        for i in range(30, -1, -1):
            # The mask helps us extract the prefix of the numbers up to bit i
            mask |= (1 << i)
            
            # Use a set to store prefixes of all numbers
            prefixes = {n & mask for n in nums}
            
            # Greedily try to set the i-th bit of max_xor to 1
            candidate = max_xor | (1 << i)
            
            for p in prefixes:
                # If (prefix ^ candidate) is also a prefix, 
                # then there exist two prefixes that XOR to the candidate
                if (p ^ candidate) in prefixes:
                    max_xor = candidate
                    break
                    
        return max_xor