import sys

# Increase recursion depth for deep trees during DFS
sys.setrecursionlimit(200_000)


class Solution:

  def palindromePath(
      self, n: int, edges: list[list[int]], s: str, queries: list[str]
  ) -> list[bool]:
    adj = [[] for _ in range(n)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)

    parent = [0] * n
    depth = [0] * n
    heavy = [-1] * n
    head = [0] * n
    pos = [0] * n
    size = [0] * n

    # First DFS to find subtree sizes, depths, parents, and heavy children
    def dfs1(u: int, p: int, d: int) -> int:
      parent[u] = p
      depth[u] = d
      sz = 1
      max_sz = 0
      for v in adj[u]:
        if v != p:
          sub_sz = dfs1(v, u, d + 1)
          sz += sub_sz
          if sub_sz > max_sz:
            max_sz = sub_sz
            heavy[u] = v
      size[u] = sz
      return sz

    dfs1(0, -1, 0)

    # Second DFS to assign segment tree indices (pos) and heavy head pointers
    cur_pos = 0

    def dfs2(u: int, h: int):
      nonlocal cur_pos
      head[u] = h
      pos[u] = cur_pos
      cur_pos += 1
      if heavy[u] != -1:
        dfs2(heavy[u], h)
      for v in adj[u]:
        if v != parent[u] and v != heavy[u]:
          dfs2(v, v)

    dfs2(0, 0)

    # Segment Tree setup for range XOR sums
    tree = [0] * (4 * n)
    vals = [1 << (ord(c) - ord("a")) for c in s]

    def build(node, start, end):
      if start == end:
        # Find node corresponding to this position
        # We can map back or just build directly using pos array
        return
      # Alternatively, initialize positions directly:
      pass

    # Better: build tree iteratively or via point updates from initial vals
    def update_tree(node, start, end, idx, val):
      if start == end:
        tree[node] = val
        return
      mid = (start + end) // 2
      if start <= idx <= mid:
        update_tree(2 * node, start, mid, idx, val)
      else:
        update_tree(2 * node + 1, mid + 1, end, idx, val)
      tree[node] = tree[2 * node] ^ tree[2 * node + 1]

    def query_tree(node, start, end, l, r):
      if r < start or end < l:
        return 0
      if l <= start and end <= r:
        return tree[node]
      mid = (start + end) // 2
      return query_tree(2 * node, start, mid, l, r) ^ query_tree(
          2 * node + 1, mid + 1, end, l, r
      )

    # Initialize segment tree with original string characters
    for i in range(n):
      update_tree(1, 0, n - 1, pos[i], vals[i])

    # Function to query path between u and v using HLD
    def query_path(u, v):
      res = 0
      while head[u] != head[v]:
        if depth[head[u]] > depth[head[v]]:
          u, v = v, u
        res ^= query_tree(1, 0, n - 1, pos[head[v]], pos[v])
        v = parent[head[v]]
      if depth[u] > depth[v]:
        u, v = v, u
      res ^= query_tree(1, 0, n - 1, pos[u], pos[v])
      return res

    answer = []
    for q in queries:
      parts = q.split()
      if parts[0] == "update":
        u = int(parts[1])
        c = parts[2]
        new_val = 1 << (ord(c) - ord("a"))
        vals[u] = new_val
        update_tree(1, 0, n - 1, pos[u], new_val)
      else:
        u = int(parts[1])
        v = int(parts[2])
        mask = query_path(u, v)
        # Check if mask has at most one bit set
        if mask == 0 or (mask & (mask - 1)) == 0:
          answer.append(True)
        else:
          answer.append(False)

    return answer