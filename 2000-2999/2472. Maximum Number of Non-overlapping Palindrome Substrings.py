class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        # dp[i] = maximum number of valid palindromes
        # using the first i characters
        dp = [0] * (n + 1)

        for end in range(n):
            # Don't select anything ending at 'end'
            dp[end + 1] = dp[end]

            # Length must be at least k
            for start in range(0, end - k + 2):
                if pal[start][end]:
                    dp[end + 1] = max(
                        dp[end + 1],
                        dp[start] + 1
                    )

        return dp[n]