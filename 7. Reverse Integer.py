class Solution:
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        rev = 0
        
        while x != 0:
            digit = int(x % 10)
            
            # Handle negative numbers correctly
            if x < 0 and digit > 0:
                digit -= 10
            
            x = (x - digit) // 10
            
            # Overflow check
            if rev > INT_MAX // 10 or rev < INT_MIN // 10:
                return 0
            
            rev = rev * 10 + digit
        
        return rev