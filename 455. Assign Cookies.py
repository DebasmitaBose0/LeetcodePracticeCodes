class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 1. Sort both greed factors and cookie sizes
        g.sort()
        s.sort()
        
        child_i = 0
        cookie_j = 0
        
        # 2. Use two pointers to find matches
        while child_i < len(g) and cookie_j < len(s):
            # If the current cookie can satisfy the current child
            if s[cookie_j] >= g[child_i]:
                # Move to the next child
                child_i += 1
            
            # Always move to the next cookie
            cookie_j += 1
            
        # The number of content children is represented by child_i
        return child_i