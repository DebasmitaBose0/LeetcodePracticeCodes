class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n)]

        for i in range(n):
            
            # Odd length palindrome
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if l == 0:
                    dp[r] = 0
                else:
                    dp[r] = min(dp[r], dp[l-1] + 1)
                l -= 1
                r += 1

            # Even length palindrome
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if l == 0:
                    dp[r] = 0
                else:
                    dp[r] = min(dp[r], dp[l-1] + 1)
                l -= 1
                r += 1

        return dp[-1]