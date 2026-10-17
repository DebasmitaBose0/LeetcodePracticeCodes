from ast import List
class Solution:

  def minSwaps(self, nums: List[int]) -> int:
    def digit_sum(n):
      s = 0
      while n > 0:
        s += n % 10
        n //= 10
      return s

    n = len(nums)
    # Store (digit_sum, value, original_index)
    indexed_nums = []
    for i, val in enumerate(nums):
      indexed_nums.append((digit_sum(val), val, i))

    # Sort based on digit sum, then value
    indexed_nums.sort(key=lambda x: (x[0], x[1]))

    # Find cycles in permutation
    visited = [False] * n
    # target_pos[i] stores the final sorted position of the element originally at i
    target_pos = [0] * n
    for new_idx, (_, _, orig_idx) in enumerate(indexed_nums):
      target_pos[orig_idx] = new_idx

    swaps = 0
    for i in range(n):
      if not visited[i] and target_pos[i] != i:
        cycle_size = 0
        curr = i
        while not visited[curr]:
          visited[curr] = True
          curr = target_pos[curr]
          cycle_size += 1
        swaps += cycle_size - 1

    return swaps