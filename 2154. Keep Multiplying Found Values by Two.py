class Solution:
    def findFinalValue(self, nums, original):
        s = set(nums)
        
        while original in s:
            original *= 2
        
        return original