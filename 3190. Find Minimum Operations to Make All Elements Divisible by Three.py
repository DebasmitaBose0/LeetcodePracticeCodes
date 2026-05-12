class Solution:
    def minimumOperations(self, nums):
        return sum(1 for x in nums if x % 3 != 0)