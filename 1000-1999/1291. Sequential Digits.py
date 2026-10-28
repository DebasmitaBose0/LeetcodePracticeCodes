from ast import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []
        
        # Determine the digit length boundaries
        min_len = len(str(low))
        max_len = len(str(high))
        
        # Explore all valid lengths
        for length in range(min_len, max_len + 1):
            # Slide a window of 'length' across the digits string
            for start in range(10 - length):
                num = int(digits[start : start + length])
                if low <= num <= high:
                    result.append(num)
                    
        return result