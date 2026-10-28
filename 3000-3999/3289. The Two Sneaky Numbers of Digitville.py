class Solution:
    def getSneakyNumbers(self, nums):
        seen = set()
        res = []
        
        for num in nums:
            if num in seen:
                res.append(num)
            else:
                seen.add(num)
        
        return res