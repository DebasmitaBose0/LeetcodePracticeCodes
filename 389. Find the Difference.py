class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_code = 0
        
        # XOR all characters in both strings
        # Characters that appear in both will cancel each other out
        for char in s:
            char_code ^= ord(char)
        for char in t:
            char_code ^= ord(char)
            
        # The remaining value is the ASCII code of the added character
        return chr(char_code)