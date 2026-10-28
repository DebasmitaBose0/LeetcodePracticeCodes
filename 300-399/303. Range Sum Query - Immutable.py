class NumArray:
    def __init__(self, nums: List[int]):
        # Create a prefix sum array where prefix[i] stores the sum of nums[0...i-1]
        # This makes the sum of range [left, right] = prefix[right + 1] - prefix[left]
        self.prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]