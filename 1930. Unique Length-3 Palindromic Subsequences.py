class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        
        for ch in set(s):
            l = s.find(ch)
            r = s.rfind(ch)
            
            if r - l > 1:
                middle = set(s[l+1:r])
                res += len(middle)
        
        return res