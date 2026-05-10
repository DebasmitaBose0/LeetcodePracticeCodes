class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        # Case 4 & 5: Edge cases for different number of digits
        candidates = {str(10**(length - 1) - 1), str(10**length + 1)}
        
        # Get the prefix (first half)
        prefix = int(n[:(length + 1) // 2])
        
        # Case 1, 2, & 3: Mirroring the prefix, prefix + 1, and prefix - 1
        for p in [prefix, prefix + 1, prefix - 1]:
            s = str(p)
            # If length is even, mirror everything. If odd, skip the last char of prefix.
            if length % 2 == 0:
                res = s + s[::-1]
            else:
                res = s + s[:-1][::-1]
            candidates.add(res)
        
        # Remove the original number from candidates
        candidates.discard(n)
        
        # Find the closest candidate
        num_n = int(n)
        closest = ""
        min_diff = float('inf')
        
        # Sort candidates numerically to handle the "smaller one" tie-break rule easily
        for cand in sorted(map(int, candidates)):
            diff = abs(cand - num_n)
            if diff < min_diff:
                min_diff = diff
                closest = str(cand)
                
        return closest