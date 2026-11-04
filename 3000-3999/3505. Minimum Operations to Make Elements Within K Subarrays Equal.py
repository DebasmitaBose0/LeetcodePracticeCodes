from ast import List
class Solution:

  def minOperations(self, nums: List[int], x: int, k: int) -> int:
    import heapq

    n = len(nums)
    if k * x > n:
      return -1

    # Step 1: Precalculate the cost for each window of size x starting at index i
    # We use two heaps to maintain the sliding window median and the sum of absolute differences.
    costs = [float('inf')] * (n - x + 1)

    # Helper data structures for the sliding window median
    left_heap = []  # max-heap (stored as negative)
    right_heap = []  # min-heap
    left_sum = 0
    right_sum = 0

    def add(val):
      nonlocal left_sum, right_sum
      if not left_heap or val <= -left_heap[0]:
        heapq.heappush(left_heap, -val)
        left_sum += val
      else:
        heapq.heappush(right_heap, val)
        right_sum += val
      balance = None
      balance()

    def remove(val):
      nonlocal left_sum, right_sum
      # Since lazy deletion or direct removal can be handled:
      # For simplicity with heaps, we can check root or use a counter/hash map,
      # but an easier approach for fixed-size sliding windows is rebuilding or using a balanced structure.
      pass  # Handled below via full window re-init or dual-heap index tracking

    # A robust way to handle sliding window median with updates:
    # Let's use a sorted list / balanced multiset equivalent or standard deque approach.
    # Given Python's standard library, maintaining a sorted list via `bisect` works well if x is small,
    # but for general constraints, a dual-heap with lazy removal is standard:

    # Let's write a clean dual-heap with lazy deletion:
    from collections import defaultdict

    L_heap, R_heap = [], []
    L_sum, R_sum = 0, 0
    removed_L = defaultdict(int)
    removed_R = defaultdict(int)

    def balance_heaps():
      nonlocal L_sum, R_sum
      # Balance sizes
      target_L_size = (x + 1) // 2
      while len(L_heap) - removed_L[L_heap[0] if L_heap else 0] > target_L_size:
        val = -heapq.heappop(L_heap)
        if removed_L[val] > 0:
          removed_L[val] -= 1
          continue
        L_sum -= val
        heapq.heappush(R_heap, val)
        R_sum += val

      while len(L_heap) - removed_L[
          L_heap[0] if L_heap else 0] < target_L_size and R_heap:
        val = heapq.heappop(R_heap)
        if removed_R[val] > 0:
          removed_R[val] -= 1
          continue
        R_sum -= val
        heapq.heappush(L_heap, -val)
        L_sum += val

      # Clean top elements if lazily removed
      while L_heap and removed_L[-L_heap[0]] > 0:
        removed_L[-L_heap[0]] -= 1
        heapq.heappop(L_heap)
      while R_heap and removed_R[R_heap[0]] > 0:
        removed_R[R_heap[0]] -= 1
        heapq.heappop(R_heap)

    def insert(val):
      nonlocal L_sum, R_sum
      if not L_heap or val <= -L_heap[0]:
        heapq.heappush(L_heap, -val)
        L_sum += val
      else:
        heapq.heappush(R_heap, val)
        R_sum += val
      balance_heaps()

    def delete(val):
      nonlocal L_sum, R_sum
      if L_heap and val <= -L_heap[0]:
        removed_L[val] += 1
        L_sum -= val
        if val == -L_heap[0]:
          while L_heap and removed_L[-L_heap[0]] > 0:
            removed_L[-L_heap[0]] -= 1
            heapq.heappop(L_heap)
      else:
        removed_R[val] += 1
        R_sum -= val
        if val == R_heap[0]:
          while R_heap and removed_R[R_heap[0]] > 0:
            removed_R[R_heap[0]] -= 1
            heapq.heappop(R_heap)
      balance_heaps()

    # Populate the first window
    for i in range(x):
      insert(nums[i])

    for i in range(n - x + 1):
      if i > 0:
        delete(nums[i - 1])
        insert(nums[i + x - 1])

      median = -L_heap[0]
      # Cost to make all elements equal to median = (elements in R * sum) - (elements in L * sum)
      # Specifically: R_sum - (count_R * median) + (count_L * median) - L_sum
      cnt_L = len(L_heap) - sum(removed_L.values())
      cnt_R = len(R_heap) - sum(removed_R.values())
      cost = (R_sum - cnt_R * median) + (cnt_L * median - L_sum)
      costs[i] = cost

    # Step 2: DP to choose k non-overlapping windows of size x
    # dp[j][i] = min cost using j windows up to index i
    # Since we only need the previous window count row, we can optimize space.
    inf = float('inf')
    dp = [inf] * (n + 1)
    # Base case: 0 windows cost 0
    dp[0] = 0

    for j in range(1, k + 1):
      next_dp = [inf] * (n + 1)
      # Minimum cost valid ending index for j windows is j * x
      min_idx = j * x
      current_min = inf

      for i in range(min_idx, n + 1):
        # Option 1: Don't start a window at i - x
        current_min = min(current_min, dp[i - x])
        # Option 2: Start a window at i - x (which covers window index i - x)
        if current_min != inf:
          next_dp[i] = current_min + costs[i - x]
        # Also propagate previous values
        if i > min_idx:
          next_dp[i] = min(next_dp[i], next_dp[i - 1])
      dp = next_dp

    return dp[n] if dp[n] != inf else -1