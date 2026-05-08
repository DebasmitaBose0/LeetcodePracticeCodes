class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 1. Sort the array to bring close numbers together
        nums.sort()
        
        # 2. Sum elements at even indices (0, 2, 4, ...)
        # These represent the min() of each adjacent pair
        return sum(nums[::2])