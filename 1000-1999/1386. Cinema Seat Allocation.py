from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Map row -> bitmask of reserved seats (focusing on seats 2 to 9)
        reserved_rows = defaultdict(int)
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                reserved_rows[r] |= (1 << (c - 1))
        
        # Start with 2 groups for every row not in reserved_rows
        ans = (n - len(reserved_rows)) * 2

        # Masks for the 4-seat blocks (1-indexed bits 2..9):
        # Left:   seats 2, 3, 4, 5 -> bits 1, 2, 3, 4 -> 0b00011110 = 0x1E = 30
        # Right:  seats 6, 7, 8, 9 -> bits 5, 6, 7, 8 -> 0b01111000 = 0x1E0 = 480 (or 0b111100000 >> 1)
        # Middle: seats 4, 5, 6, 7 -> bits 3, 4, 5, 6 -> 0b01111000 = 0x78 = 120
        LEFT_MASK = (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4)      # seats 2, 3, 4, 5
        RIGHT_MASK = (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8)    # seats 6, 7, 8, 9
        MID_MASK = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6)      # seats 4, 5, 6, 7

        for mask in reserved_rows.values():
            count = 0
            left_ok = not (mask & LEFT_MASK)
            right_ok = not (mask & RIGHT_MASK)
            
            if left_ok and right_ok:
                count = 2
            elif left_ok or right_ok or not (mask & MID_MASK):
                count = 1
                
            ans += count

        return ans