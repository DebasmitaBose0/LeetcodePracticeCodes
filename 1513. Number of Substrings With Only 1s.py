class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = res = 0
        
        for ch in s:
            if ch == '1':
                count += 1
                res += count
            else:
                count = 0
        
        return res % MOD