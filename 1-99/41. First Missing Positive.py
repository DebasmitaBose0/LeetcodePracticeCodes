class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Step 1: Place numbers at correct index
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Step 2: Find missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1