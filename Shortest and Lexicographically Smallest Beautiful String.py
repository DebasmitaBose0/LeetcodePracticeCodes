class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        min_len = float('inf')
        
        l = 0
        ones_count = 0
        
        for r in range(n):
            if s[r] == '1':
                ones_count += 1
            
            # Shrink the window from the left while it has k ones
            while ones_count == k:
                current_sub = s[l:r+1]
                curr_len = len(current_sub)
                
                # Update if we found a shorter string, or a lexicographically smaller one of the same length
                if curr_len < min_len:
                    min_len = curr_len
                    ans = current_sub
                elif curr_len == min_len:
                    if ans == "" or current_sub < ans:
                        ans = current_sub
                
                if s[l] == '1':
                    ones_count -= 1
                l += 1
                
        return ans