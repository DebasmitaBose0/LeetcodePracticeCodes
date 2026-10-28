from ast import List
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        has_non_zero = False

        for num in nums:
            total_xor ^= num
            if num != 0:
                has_non_zero = True

        # If every element is 0, no non-zero XOR subsequence can be formed
        if not has_non_zero:
            return 0

        # If the XOR of the entire array is already non-zero, take all elements
        if total_xor != 0:
            return len(nums)

        # If total XOR is 0, excluding any non-zero element x gives XOR = 0 ^ x = x != 0
        return len(nums) - 1