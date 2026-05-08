class Solution:
    def minimumPrefixLength(self, nums):
        n = len(nums)
        i = n - 1
        
        while i > 0 and nums[i-1] < nums[i]:
            i -= 1
        
        return i