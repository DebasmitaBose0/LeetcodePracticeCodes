from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counts = defaultdict(int)
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            counts[char] += 1
            
            # Shrink from the left if any character appears more than twice
            while counts[char] > 2:
                counts[s[left]] -= 1
                left += 1
            
            # Update the maximum length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len