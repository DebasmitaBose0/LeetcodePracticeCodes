class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_len = 1    # Start with 1-digit numbers (1-9)
        count = 9        # There are 9 such numbers
        start = 1        # The first number of this length
        
        # Step 1: Identify the length of the number that contains the nth digit
        while n > digit_len * count:
            n -= digit_len * count
            digit_len += 1
            count *= 10
            start *= 10
            
        # Step 2: Find the actual number
        # (n - 1) because we are using 0-based indexing to find the offset
        target_num = start + (n - 1) // digit_len
        
        # Step 3: Find the digit within that number
        target_idx = (n - 1) % digit_len
        return int(str(target_num)[target_idx])