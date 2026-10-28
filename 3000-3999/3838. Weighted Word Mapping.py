from ast import List
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        
        for word in words:
            # 1. Calculate the total weight of the current word
            word_weight = sum(weights[ord(char) - ord('a')] for char in word)
            
            # 2. Take the weight modulo 26
            mod_val = word_weight % 26
            
            # 3. Map to reverse alphabetical order (0 -> 'z', 1 -> 'y', ..., 25 -> 'a')
            mapped_char = chr(ord('z') - mod_val)
            
            result.append(mapped_char)
            
        # 4. Return the concatenated string
        return "".join(result)