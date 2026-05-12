class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Handle negative numbers
        is_negative = num < 0
        num = abs(num)
        
        res = []
        while num:
            # Get the remainder (base 7 digit)
            res.append(str(num % 7))
            # Get the quotient for the next iteration
            num //= 7
            
        # Join digits in reverse order and add negative sign if needed
        return ("-" if is_negative else "") + "".join(reversed(res))