class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        # Option 1: Product of the 3 largest numbers
        # Option 2: Product of the 2 smallest numbers and the largest number
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])