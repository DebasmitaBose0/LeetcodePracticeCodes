class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # If lengths don't match, they can't follow the same pattern
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        # zip pairs the character and word at the same index
        for char, word in zip(pattern, words):
            # Check if char is already mapped to a different word
            if char in char_to_word and char_to_word[char] != word:
                return False
            
            # Check if word is already mapped to a different char
            if word in word_to_char and word_to_char[word] != char:
                return False
            
            # Establish the mapping
            char_to_word[char] = word
            word_to_char[word] = char
            
        return True