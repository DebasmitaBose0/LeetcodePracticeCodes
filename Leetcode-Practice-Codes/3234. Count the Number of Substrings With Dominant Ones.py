class Solution:
    def numberOfSubstrings(self, s):
        n = len(s)
        pref = [0]*(n+1)
        
        for i in range(n):
            pref[i+1] = pref[i] + (s[i] == '1')
        
        res = 0
        
        for z in range(0, int(n**0.5) + 2):
            l = 0
            for r in range(n):
                while l <= r:
                    zeros = (r - l + 1) - (pref[r+1] - pref[l])
                    if zeros > z:
                        l += 1
                    else:
                        break
                
                zeros = (r - l + 1) - (pref[r+1] - pref[l])
                ones = pref[r+1] - pref[l]
                
                if zeros == z and ones >= z*z:
                    res += 1
        
        return res