class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Helper to find changes needed to make a string a palindrome
        def min_palin_changes(sub):
            changes = 0
            left, right = 0, len(sub) - 1
            while left < right:
                if sub[left] != sub[right]:
                    changes += 1
                left += 1
                right -= 1
            return changes

        # Precompute divisors for each length up to n
        divisors = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)

        # cost[i][j] = min changes to make s[i..j] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = float('inf')
                
                for d in divisors[length]:
                    current_d_changes = 0
                    # Check each of the d groups
                    for g in range(d):
                        group_str = "".join(s[i + g + c * d] for c in range(length // d))
                        current_d_changes += min_palin_changes(group_str)
                    min_changes = min(min_changes, current_d_changes)
                
                cost[i][j] = min_changes

        # DP table: dp[i][rem] -> min cost to partition s[i:] into rem parts
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[n][0] = 0

        for rem in range(1, k + 1):
            for i in range(n):
                # We need enough characters left to form 'rem' parts of at least length 2
                for x in range(i, n - (rem - 1)):
                    if cost[i][x] != float('inf') and dp[x + 1][rem - 1] != float('inf'):
                        dp[i][rem] = min(dp[i][rem], cost[i][x] + dp[x + 1][rem - 1])

        return dp[0][k]