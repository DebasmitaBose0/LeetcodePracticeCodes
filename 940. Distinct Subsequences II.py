class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            # Calculate total subsequences we can form ending with 'char'
            total = sum(dp) % MOD
            # Update the dp value for the current character, subtracting previous contributions to avoid duplicates
            dp[idx] = (total + 1) % MOD
            
        return sum(dp) % MOD