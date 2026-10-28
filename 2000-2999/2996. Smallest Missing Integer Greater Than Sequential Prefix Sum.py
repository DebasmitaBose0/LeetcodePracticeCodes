class Solution:

    def missingInteger(self, nums: list[int]) -> int:
        # Find the end of the longest sequential prefix starting at index 0
        i = 0
        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
            i += 1

        # Calculate the sum of the longest sequential prefix
        s = sum(nums[: i + 1])

        # Store nums elements in a set for O(1) lookup
        num_set = set(nums)

        # Find the smallest integer x >= s missing from nums
        while s in num_set:
            s += 1

        return s