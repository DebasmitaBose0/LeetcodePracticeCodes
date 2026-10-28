class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Step 1: Track the length of the result string after each operation
        lengths = []
        curr_len = 0
        
        for char in s:
            if char.islower():
                curr_len += 1
            elif char == '*':
                if curr_len > 0:
                    curr_len -= 1
            elif char == '#':
                curr_len *= 2
            elif char == '%':
                # Reversing a string keeps its length identical
                pass
            lengths.append(curr_len)
        
        # If k is completely out of bounds of the final string length
        if k >= curr_len:
            return "."
            
        # Step 2: Walk backwards through the string s to pinpoint index k
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            
            if char == '#':
                # The length before this duplication operation
                prev_len = lengths[i-1] if i > 0 else 0
                # If k falls in the duplicated second half, map it to the first half
                if k >= prev_len:
                    k %= prev_len
                    
            elif char == '%':
                # The length remains the same before/after '%'
                prev_len = lengths[i-1] if i > 0 else 0
                # Mirror the index across the midpoint
                k = prev_len - 1 - k
                
            elif char == '*':
                # A delete operation means the character *before* this step 
                # existed, but it doesn't shift our target index k.
                pass
                
            else:  # It's a lowercase English letter
                prev_len = lengths[i-1] if i > 0 else 0
                # If our target index k matches the newly appended character's index
                if k == prev_len:
                    return char
                    
        return "."