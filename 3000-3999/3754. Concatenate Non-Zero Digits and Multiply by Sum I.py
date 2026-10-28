class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Edge case for 0
        if n == 0:
            return 0
            
        x = 0
        digit_sum = 0
        multiplier = 1
        
        while n > 0:
            digit = n % 10
            if digit != 0:
                # Build x from right to left
                x = digit * multiplier + x
                multiplier *= 10
                # Track the sum of digits simultaneously
                digit_sum += digit
            n //= 10
            
        return x * digit_sum