class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        size = len(digits)
        
        # 1. Find the first decreasing element from the right
        i = size - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
            
        if i == -1:
            return -1
            
        # 2. Find the smallest element to the right of i that is larger than digits[i]
        j = size - 1
        while digits[j] <= digits[i]:
            j -= 1
            
        # 3. Swap them
        digits[i], digits[j] = digits[j], digits[i]
        
        # 4. Reverse the suffix (everything after index i)
        digits[i+1:] = digits[i+1:][::-1]
        
        res = int("".join(digits))
        
        # 5. Check for 32-bit integer overflow
        return res if res <= 2**31 - 1 else -1