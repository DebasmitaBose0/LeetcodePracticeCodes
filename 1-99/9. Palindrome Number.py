class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge cases
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10
        
        # For even digits: x == reversed_half
        # For odd digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10