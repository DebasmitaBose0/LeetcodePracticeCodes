class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        # dp[i] is the length of the longest valid subsequence of columns ending at i
        dp = [1] * m
        
        for i in range(1, m):
            for j in range(i):
                # Check if column i can follow column j for ALL rows
                if all(strs[k][j] <= strs[k][i] for k in range(n)):
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Max columns kept = max(dp). Min deleted = total - max_kept.
        return m - max(dp)