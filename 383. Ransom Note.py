from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the frequency of each character in the magazine
        magazine_counts = Counter(magazine)
        
        # Iterate through each character needed for the ransom note
        for char in ransomNote:
            # If the character is not available or exhausted
            if magazine_counts[char] <= 0:
                return False
            # "Use" one instance of the character
            magazine_counts[char] -= 1
            
        return True