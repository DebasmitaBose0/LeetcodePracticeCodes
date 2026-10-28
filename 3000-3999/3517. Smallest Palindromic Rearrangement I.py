class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half_len = n // 2
        
        # Take the first half and sort it lexicographically
        first_half = sorted(s[:half_len])
        
        # Determine the middle character if n is odd
        mid = s[half_len] if n % 2 != 0 else ""
        
        # Construct the palindrome
        return "".join(first_half) + mid + "".join(reversed(first_half))