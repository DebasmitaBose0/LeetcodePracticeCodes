class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Map to store the maximum length for each unique bitmask
        mask_map = {}
        
        for word in words:
            mask = 0
            for char in word:
                # Create a bitmask for the word
                mask |= (1 << (ord(char) - ord('a')))
            
            # If multiple words have the same mask, only keep the longest length
            mask_map[mask] = max(mask_map.get(mask, 0), len(word))
            
        max_prod = 0
        
        # Compare all pairs of unique masks
        masks = list(mask_map.keys())
        for i in range(len(masks)):
            for j in range(i + 1, len(masks)):
                # If AND is 0, they share no common characters
                if masks[i] & masks[j] == 0:
                    max_prod = max(max_prod, mask_map[masks[i]] * mask_map[masks[j]])
                    
        return max_prod