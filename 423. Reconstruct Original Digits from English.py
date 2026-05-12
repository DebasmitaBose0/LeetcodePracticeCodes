from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        # Count frequency of every character in s
        counts = Counter(s)
        
        # Array to store frequency of each digit 0-9
        out = [0] * 10
        
        # Level 1: Unique characters
        out[0] = counts['z']
        out[2] = counts['w']
        out[4] = counts['u']
        out[6] = counts['x']
        out[8] = counts['g']
        
        # Level 2: Shared characters (subtraction logic)
        out[3] = counts['h'] - out[8]
        out[5] = counts['f'] - out[4]
        out[7] = counts['s'] - out[6]
        
        # Level 3: Remaining
        out[1] = counts['o'] - out[0] - out[2] - out[4]
        out[9] = counts['i'] - out[5] - out[6] - out[8]
        
        # Build the final ascending string
        result = []
        for i in range(10):
            result.append(str(i) * out[i])
            
        return "".join(result)