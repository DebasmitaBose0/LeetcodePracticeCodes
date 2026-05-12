class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Hex characters mapping
        chars = "0123456789abcdef"
        
        # Convert to 32-bit unsigned equivalent
        # This handles the two's complement for negative numbers
        num &= 0xffffffff
        
        res = []
        while num > 0:
            # Extract the last 4 bits and map to hex char
            res.append(chars[num & 0xf])
            # Shift right by 4 bits to move to the next hex digit
            num >>= 4
            
        # Since we appended from right to left, reverse the string
        return "".join(reversed(res))