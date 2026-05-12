class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        
        upper_limit = 10**n - 1
        lower_limit = 10**(n-1)
        
        # Start from the largest possible half of the palindrome
        for half in range(upper_limit, lower_limit - 1, -1):
            # Construct the palindrome (e.g., 99 -> 9999, 98 -> 9889)
            s = str(half)
            palindrome = int(s + s[::-1])
            
            # Check if this palindrome can be factored
            # We only need to check divisors from upper_limit down to sqrt(palindrome)
            for d in range(upper_limit, int(palindrome**0.5), -1):
                if palindrome % d == 0:
                    # If palindrome / d is also within the n-digit range
                    if lower_limit <= palindrome // d <= upper_limit:
                        return palindrome % 1337
        
        return -1