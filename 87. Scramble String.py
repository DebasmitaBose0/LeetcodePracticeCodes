class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        
        def dfs(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            
            # Base case
            if a == b:
                return True
            
            # Prune: different characters
            if sorted(a) != sorted(b):
                return False
            
            n = len(a)
            
            for i in range(1, n):
                # Case 1: no swap
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                
                # Case 2: swap
                if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):
                    memo[(a, b)] = True
                    return True
            
            memo[(a, b)] = False
            return False
        
        return dfs(s1, s2)