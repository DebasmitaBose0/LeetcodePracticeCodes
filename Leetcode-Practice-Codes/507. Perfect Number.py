import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Perfect numbers must be positive and greater than 1 
        # (1 is not a perfect number because its only divisor is itself)
        if num <= 1:
            return False
        
        # Start with 1 as it is a divisor for every number > 1
        divisor_sum = 1
        
        # Check divisors from 2 up to sqrt(num)
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisor_sum += i
                # If the paired divisor (num/i) is different from i, add it too
                if i * i != num:
                    divisor_sum += num // i
                    
        return divisor_sum == num