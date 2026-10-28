from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # handle cases where k > n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse(0, n-1)
        # Step 2: Reverse first k elements
        reverse(0, k-1)
        # Step 3: Reverse remaining n-k elements
        reverse(k, n-1)