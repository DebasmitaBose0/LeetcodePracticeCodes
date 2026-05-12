class Solution:
    def maxOperations(self, s: str) -> int:
        res = 0
        ones = 0
        n = len(s)
        
        for i in range(n):
            if s[i] == '1':
                # Increment the count of 1s encountered
                ones += 1
            elif i > 0 and s[i-1] == '1':
                # We found a '0' and the previous char was '1'
                # This indicates a new block of zeros that all 
                # previous '1's can jump over.
                res += ones
                
        return res