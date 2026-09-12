from bisect import bisect_right
from typing import List


class Solution:

  def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
    n = len(intervals)
    # Augment intervals with their original indices
    ext_intervals = []
    for i, (l, r, w) in enumerate(intervals):
      ext_intervals.append((l, r, w, i))

    # Sort by right endpoint, then weight, then original index
    ext_intervals.sort(key=lambda x: (x[1], x[2], x[3]))

    # Extract right endpoints for binary search
    rights = [item[1] for item in ext_intervals]

    # dp[c] stores (max_weight, list_of_indices)
    # We can use memoization or iterative DP with up to 4 intervals.
    # To optimize space, we can store for each prefix and count.
    # Given constraints, let's build the DP tables efficiently.

    memo = {}

    def solve():
      # dp table: dp[i][c] = (weight, indices_tuple)
      # i from 0 to n, c from 0 to 4
      dp = [[(-1, ()) for _ in range(5)] for _ in range(n + 1)]
      for i in range(n + 1):
        dp[i][0] = (0, ())

      # Precompute previous non-overlapping indices using binary search
      prev_idx = [-1] * n
      for i in range(n):
        l_i = ext_intervals[i][0]
        # Find rightmost interval whose right endpoint < l_i
        # Equivalent to bisect_right where we look for elements with r < l_i
        # Since ext_intervals is sorted by right endpoint:
        idx = bisect_right(rights, l_i - 1)
        prev_idx[i] = idx - 1  # 0-indexed in sorted array

      for i in range(1, n + 1):
        l, r, w, orig_idx = ext_intervals[i - 1]
        p = prev_idx[i - 1]

        for c in range(1, 5):
          # Option 1: Skip current interval
          best_w, best_inds = dp[i - 1][c]

          # Option 2: Include current interval
          if c > 0:
            prev_w, prev_inds = dp[p + 1][c - 1] if p >= -1 else (0, ())
            if prev_w != -1:
              curr_w = prev_w + w
              curr_inds = prev_inds + (orig_idx,)

              # Compare with option 1
              if curr_w > best_w:
                best_w = curr_w
                best_inds = curr_inds
              elif curr_w == best_w and best_inds:
                # Lexicographical comparison
                if curr_inds < best_inds:
                  best_inds = curr_inds

          dp[i][c] = (best_w, best_inds)

      # Find the best result across all counts (up to 4)
      max_w = -1
      best_res = ()
      for c in range(5):
        w_val, inds = dp[n][c]
        if w_val > max_w:
          max_w = w_val
          best_res = inds
        elif w_val == max_w and best_res:
          if inds < best_res:
            best_res = inds

      return sorted(list(best_res))

    return solve()