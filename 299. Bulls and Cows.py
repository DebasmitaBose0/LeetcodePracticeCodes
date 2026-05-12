from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        
        s_count = Counter()
        g_count = Counter()
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                # Track counts of non-bull digits
                s_count[s] += 1
                g_count[g] += 1
        
        # Cows are the overlap of remaining digit counts
        for char in s_count:
            if char in g_count:
                cows += min(s_count[char], g_count[char])
                
        return f"{bulls}A{cows}B"