class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        ans = 0
        n = len(s)
        
        for right in range(n):
            # Expand the window by adding the current character
            count[s[right]] += 1
            
            # Shrink the window from the left as long as it remains valid
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                # If s[left...right] is valid, then s[left...right], s[left...right+1], 
                # ..., s[left...n-1] are all valid substrings.
                ans += n - right
                
                # Remove the character at the left pointer and move it forward
                count[s[left]] -= 1
                left += 1
                
        return ans