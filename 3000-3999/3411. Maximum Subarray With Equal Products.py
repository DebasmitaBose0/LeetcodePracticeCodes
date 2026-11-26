import math
from typing import List


class Solution:

    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1  # Any single positive element forms a valid subarray of length 1

        for i in range(n):
            prod = 1
            curr_gcd = 0
            curr_lcm = 1

            for j in range(i, n):
                x = nums[j]
                prod *= x
                curr_gcd = x if curr_gcd == 0 else math.gcd(curr_gcd, x)
                curr_lcm = math.lcm(curr_lcm, x)

                if prod == curr_lcm * curr_gcd:
                    ans = max(ans, j - i + 1)

        return ans