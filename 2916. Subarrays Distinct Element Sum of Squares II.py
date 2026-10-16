class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def _push(self, node, left, right):
        if self.lazy[node] != 0:
            val = self.lazy[node]
            mid = (left + right) // 2
            
            # Left child update
            self.tree[2 * node] = (self.tree[2 * node] + val * (mid - left + 1)) % self.MOD
            self.lazy[2 * node] = (self.lazy[2 * node] + val) % self.MOD
            
            # Right child update
            self.tree[2 * node + 1] = (self.tree[2 * node + 1] + val * (right - mid)) % self.MOD
            self.lazy[2 * node + 1] = (self.lazy[2 * node + 1] + val) % self.MOD
            
            self.lazy[node] = 0

    def update(self, node, left, right, q_left, q_right, val):
        if q_left > right or q_right < left:
            return
        if q_left <= left and right <= q_right:
            self.tree[node] = (self.tree[node] + val * (right - left + 1)) % self.MOD
            self.lazy[node] = (self.lazy[node] + val) % self.MOD
            return
        
        self._push(node, left, right)
        mid = (left + right) // 2
        self.update(2 * node, left, mid, q_left, q_right, val)
        self.update(2 * node + 1, mid + 1, right, q_left, q_right, val)
        self.tree[node] = (self.tree[2 * node] + self.tree[2 * node + 1]) % self.MOD

    def query(self, node, left, right, q_left, q_right):
        if q_left > right or q_right < left:
            return 0
        if q_left <= left and right <= q_right:
            return self.tree[node]
        
        self._push(node, left, right)
        mid = (left + right) // 2
        res_left = self.query(2 * node, left, mid, q_left, q_right)
        res_right = self.query(2 * node + 1, mid + 1, right, q_left, q_right)
        return (res_left + res_right) % self.MOD


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        seg_tree = SegmentTree(n)
        
        last_seen = {}
        total_sum = 0
        current_sum_squares = 0
        
        for i, x in enumerate(nums):
            prev = last_seen.get(x, -1)
            last_seen[x] = i
            
            # Range update for L from prev + 1 to i
            # We add 2 * sum + length to sum of squares because (s+1)^2 = s^2 + 2s + 1
            if prev < i:
                range_sum = seg_tree.query(1, 0, n - 1, prev + 1, i)
                seg_tree.update(1, 0, n - 1, prev + 1, i, 1)
                current_sum_squares = (current_sum_squares + 2 * range_sum + (i - prev)) % MOD
            
            total_sum = (total_sum + current_sum_squares) % MOD
            
        return total_sum