class Solution:
    def minOperations(self, nums, target):
        return len({nums[i] for i in range(len(nums)) if nums[i] != target[i]})