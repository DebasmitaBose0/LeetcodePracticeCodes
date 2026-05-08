class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Case 1: All letters are capitals
        if word.isupper():
            return True
        
        # Case 2: All letters are lowercase
        if word.islower():
            return True
        
        # Case 3: Only the first letter is capital (Title Case)
        if word.istitle():
            return True
        
        return False