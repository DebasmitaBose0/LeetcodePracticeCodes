class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert string to list because strings are immutable
        chars = list(s)
        
        # Iterate through the string in chunks of 2k
        for i in range(0, len(chars), 2 * k):
            # Reverse the first k characters of the current 2k block
            # chars[i:i+k] selects the segment to reverse
            # [::-1] reverses that segment
            chars[i:i+k] = chars[i:i+k][::-1]
            
        return "".join(chars)