class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # If s = "abab", s + s = "abababab"
        # Removing first and last: "bababa"
        # "abab" exists in "bababa" -> return True
        
        return s in (s + s)[1:-1]