class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        remaining = n
        left_to_right = True
        
        while remaining > 1:
            # We update the head in two cases:
            # 1. We are moving from left to right (the first element is always removed)
            # 2. We are moving from right to left AND the number of elements is odd
            if left_to_right or remaining % 2 == 1:
                head += step
            
            # After each pass:
            remaining //= 2   # Half the elements are gone
            step *= 2         # The gap between remaining elements doubles
            left_to_right = not left_to_right # Flip the direction
            
        return head