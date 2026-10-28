class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Base case: if the string is too short to satisfy the condition
        if len(s) < k:
            return 0
        
        # 1. Count the frequency of every character in the current substring
        for char in set(s):
            # 2. Identify a "split character" (one that appears less than k times)
            if s.count(char) < k:
                # 3. This character can never be part of a valid substring.
                # Use it as a delimiter to split the string into segments.
                # We return the maximum result from any of these segments.
                return max(self.longestSubstring(sub, k) for sub in s.split(char))
        
        # 4. If no character was found with frequency < k, the entire string is valid
        return len(s)