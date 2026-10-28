class Solution:
    def alternatingXOR(self, nums, target1, target2):
        MOD = 10**9 + 7
        
        dp1 = {0: 1}  # expecting target1
        dp2 = {}
        
        px = 0
        res = 0
        
        for num in nums:
            px ^= num
            
            ways1 = dp1.get(px ^ target1, 0)
            ways2 = dp2.get(px ^ target2, 0)
            
            dp2[px] = (dp2.get(px, 0) + ways1) % MOD
            dp1[px] = (dp1.get(px, 0) + ways2) % MOD
            
            res = (res + ways1) % MOD
        
        return res