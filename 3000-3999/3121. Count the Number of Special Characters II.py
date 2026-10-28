class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Maps to store indices
        # last_lower: tracks the LAST occurrence of a lowercase character
        # first_upper: tracks the FIRST occurrence of an uppercase character
        last_lower = {}
        first_upper = {}
        
        # A set to keep track of characters that became invalid 
        # because a lowercase instance appeared after an uppercase instance
        invalidated = set()
        
        for i, char in enumerate(word):
            if char.islower():
                # If we already saw the uppercase version, this lowercase placement is invalid
                if char.upper() in first_upper:
                    invalidated.add(char)
                last_lower[char] = i
            else:
                # We only care about the FIRST occurrence of the uppercase character
                if char not in first_upper:
                    first_upper[char] = i
                    
        special_count = 0
        
        # Check all lowercase characters we've tracked
        for lower_char, lower_idx in last_lower.items():
            upper_char = lower_char.upper()
            
            # Condition: must not be invalidated, must exist in uppercase, 
            # and last lowercase index must be before first uppercase index
            if (lower_char not in invalidated and 
                upper_char in first_upper and 
                lower_idx < first_upper[upper_char]):
                special_count += 1
                
        return special_count