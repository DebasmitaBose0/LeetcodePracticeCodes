from collections import Counter
from typing import List


class Solution:

  def largestInteger(self, nums: List[int], k: int) -> int:
    n = len(nums)
    counts = Counter(nums)

    # Case 1: Subarray size is 1
    if k == 1:
      unique = [x for x, count in counts.items() if count == 1]
      return max(unique) if unique else -1

    # Case 2: Subarray size is equal to array length
    if k == n:
      return max(nums)

    # Case 3: 1 < k < n (only boundary elements are candidates)
    ans = -1
    if counts[nums[0]] == 1:
      ans = max(ans, nums[0])
    if counts[nums[-1]] == 1:
      ans = max(ans, nums[-1])

    return ans