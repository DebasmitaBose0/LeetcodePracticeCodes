class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # Split the strings to get real and imaginary parts
        # num1 is "a+bi", num2 is "c+di"
        a, b_str = num1.split('+')
        c, d_str = num2.split('+')
        
        # Convert to integers (removing the 'i' from the imaginary parts)
        a = int(a)
        b = int(b_str[:-1])
        c = int(c)
        d = int(d_str[:-1])
        
        # Apply the formula: (ac - bd) + (ad + bc)i
        real_part = (a * c) - (b * d)
        imag_part = (a * d) + (b * c)
        
        # Return the formatted string
        return f"{real_part}+{imag_part}i"