class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # If there aren't enough 1's in the entire string, return empty
        if s.count('1') < k:
            return ""
        
        n = len(s)
        best_res = ""
        left = 0
        ones_count = 0
        
        for right in range(n):
            if s[right] == '1':
                ones_count += 1
            
            # When we have exactly k ones, try to minimize the window
            while ones_count == k:
                # Potential beautiful substring
                current_sub = s[left : right + 1]
                
                # Update best_res if current_sub is shorter or lexicographically smaller
                if not best_res or len(current_sub) < len(best_res):
                    best_res = current_sub
                elif len(current_sub) == len(best_res):
                    if current_sub < best_res:
                        best_res = current_sub
                
                # Move left pointer to look for smaller windows or next candidates
                if s[left] == '1':
                    ones_count -= 1
                left += 1
                
        return best_res