from ast import List
class Solution:

  def countServers(
      self, n: int, logs: List[List[int]], x: int, queries: List[int]
  ) -> List[int]:
    # Sort logs by time
    logs.sort(key=lambda x: x[1])

    # Pair each query with its original index so we can restore the order later
    indexed_queries = sorted(
        [(q, i) for i, q in enumerate(queries)], key=lambda x: x[0]
    )

    res = [0] * len(queries)
    server_count = {}
    unique_active = 0

    log_idx = 0
    num_logs = len(logs)

    # Sliding window pointers for logs
    left = 0
    right = 0

    for q, original_idx in indexed_queries:
      window_start = q - x
      window_end = q

      # Expand right pointer to include logs up to window_end
      while right < num_logs and logs[right][1] <= window_end:
        s_id = logs[right][0]
        if server_count.get(s_id, 0) == 0:
          unique_active += 1
        server_count[s_id] = server_count.get(s_id, 0) + 1
        right += 1

      # Shrink left pointer to remove logs older than window_start
      while left < num_logs and logs[left][1] < window_start:
        s_id = logs[left][0]
        server_count[s_id] -= 1
        if server_count[s_id] == 0:
          unique_active -= 1
        left += 1

      # Total servers minus active servers gives zero-request servers
      res[original_idx] = n - unique_active

    return res