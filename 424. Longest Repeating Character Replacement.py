class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        left = 0
        max_freq = 0
        for right in range(len(s)):
            # Add the new character to the frequency map
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # Update the maximum frequency found in the current window
            max_freq = max(max_freq, count[s[right]])
            
            # If the number of characters to replace exceeds k, shrink window
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            # The result is the maximum window size seen
            res = max(res, right - left + 1)
            
        return res