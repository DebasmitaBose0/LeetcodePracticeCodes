from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digit_count = Counter(digits)
        count = 0
        
        # Check all 3-digit even numbers
        for num in range(100, 1000, 2):
            # Extract the digits of the current number
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            # Count the frequency required for this number
            req = Counter([d1, d2, d3])
            
            # Check if we have enough of each digit in our input array
            if all(digit_count[d] >= req[d] for d in req):
                count += 1
                
        return count