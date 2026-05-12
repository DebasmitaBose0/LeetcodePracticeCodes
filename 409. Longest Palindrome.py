from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        has_odd = False
        
        for count in counts.values():
            if count % 2 == 0:
                length += count
            else:
                # Add the largest even part
                length += count - 1
                has_odd = True
        
        # If there's at least one odd frequency, we can put one char in the center
        return length + 1 if has_odd else length