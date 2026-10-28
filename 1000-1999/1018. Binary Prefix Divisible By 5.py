class Solution:
    def prefixesDivBy5(self, nums):
        res = []
        curr = 0
        
        for bit in nums:
            curr = (curr * 2 + bit) % 5
            res.append(curr == 0)
        
        return res