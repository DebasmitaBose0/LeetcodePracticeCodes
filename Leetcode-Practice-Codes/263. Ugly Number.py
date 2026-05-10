class Solution:
    def isUgly(self, n: int) -> bool:
        # Ugly numbers must be positive
        if n <= 0:
            return False
        
        # Repeatedly divide by 2, 3, and 5
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        
        # If the remaining number is 1, it only had factors of 2, 3, and 5
        return n == 1