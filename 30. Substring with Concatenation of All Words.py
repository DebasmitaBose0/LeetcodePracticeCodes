from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        
        word_map = Counter(words)
        result = []
        
        # Try all offsets
        for i in range(word_len):
            left = i
            curr_map = Counter()
            count = 0
            
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                
                if word in word_map:
                    curr_map[word] += 1
                    count += 1
                    
                    # If too many of a word → shrink
                    while curr_map[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        curr_map[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    # Found valid window
                    if count == word_count:
                        result.append(left)
                        
                        # Move forward
                        left_word = s[left:left + word_len]
                        curr_map[left_word] -= 1
                        left += word_len
                        count -= 1
                
                else:
                    # Reset window
                    curr_map.clear()
                    count = 0
                    left = right + word_len
        
        return result