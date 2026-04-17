class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Define the three rows of the American keyboard as sets
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        
        for word in words:
            # Convert the word to lowercase and turn it into a set of characters
            lower_word_set = set(word.lower())
            
            # Check if the word's characters are a subset of any of the rows
            if lower_word_set <= row1 or lower_word_set <= row2 or lower_word_set <= row3:
                result.append(word)
                
        return result