from collections import defaultdict
from typing import List


class Solution:
    def subtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        orig_adj = defaultdict(list)
        for node in range(1, n):
            orig_adj[parent[node]].append(node)

        new_parent = parent[:]
        last_seen = [-1] * 26

        # Pass 1: find closest ancestor with the same character
        def find_ancestors(u: int) -> None:
            idx = ord(s[u]) - ord('a')
            prev_ancestor = last_seen[idx]
            if prev_ancestor != -1:
                new_parent[u] = prev_ancestor

            last_seen[idx] = u
            for v in orig_adj[u]:
                find_ancestors(v)
            last_seen[idx] = prev_ancestor  # backtrack

        find_ancestors(0)

        # Pass 2: build the re-parented tree and compute subtree sizes
        new_adj = defaultdict(list)
        for node in range(1, n):
            new_adj[new_parent[node]].append(node)

        ans = [0] * n

        def calc_size(u: int) -> int:
            size = 1
            for v in new_adj[u]:
                size += calc_size(v)
            ans[u] = size
            return size

        calc_size(0)
        return ans