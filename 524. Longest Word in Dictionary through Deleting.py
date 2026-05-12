class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        best_word = ""
        
        for word in dictionary:
            # Optimization: Skip if the word is shorter than our current best
            # or if it's the same length but lexicographically larger
            if len(word) < len(best_word) or (len(word) == len(best_word) and word > best_word):
                continue
            
            # Two-pointer check to see if 'word' is a subsequence of 's'
            s_ptr = 0
            w_ptr = 0
            while s_ptr < len(s) and w_ptr < len(word):
                if s[s_ptr] == word[w_ptr]:
                    w_ptr += 1
                s_ptr += 1
            
            # If we matched all characters of 'word'
            if w_ptr == len(word):
                best_word = word
                
        return best_word