class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Find the index of 0
        k = nums.index(0)

        # Check Case 1: Elements are arranged in cyclic increasing order
        # Expected: nums[i] == (i - k + n) % n
        is_increasing = all(nums[i] == (i - k + n) % n for i in range(n))
        if is_increasing:
            if k == 0:
                return 0
            # Option 1: Rotate left k times -> k
            # Option 2: Reverse, rotate left (n - k) times, reverse -> 2 + (n - k)
            return min(k, 2 + n - k)

        # Check Case 2: Elements are arranged in cyclic decreasing order
        # Expected: nums[i] == (k - i + n) % n
        is_decreasing = all(nums[i] == (k - i + n) % n for i in range(n))
        if is_decreasing:
            # Option 1: Reverse first, then rotate left (n - 1 - k) times -> 1 + (n - 1 - k) = n - k
            # Option 2: Rotate left (k + 1) times, then reverse -> (k + 1) + 1 = k + 2
            return min(n - k, k + 2)

        # If it doesn't match either cyclic order, it is impossible to sort
        return -1