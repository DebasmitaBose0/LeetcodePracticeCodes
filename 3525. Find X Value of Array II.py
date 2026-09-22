class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.nums = nums
        # Each node stores:
        # - remain: frequency array of size k for prefix product remainders
        # - prod: total product of the segment modulo k
        self.tree_remain = [[0] * k for _ in range(4 * self.n)]
        self.tree_prod = [1] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def _combine(self, left_rem, left_prod, right_rem, right_prod):
        res_rem = [0] * self.k
        # Elements entirely inside the left segment keep their remainder distribution
        for i in range(self.k):
            res_rem[i] = left_rem[i]
        
        # Elements in the right segment are scaled by the product of the left segment
        for i in range(self.k):
            if right_rem[i] > 0:
                new_rem = (i * left_prod) % self.k
                res_rem[new_rem] += right_rem[i]
                
        res_prod = (left_prod * right_prod) % self.k
        return res_rem, res_prod

    def build(self, node, start, end):
        if start == end:
            rem = self.nums[start] % self.k
            self.tree_remain[node] = [0] * self.k
            self.tree_remain[node][rem] = 1
            self.tree_prod[node] = rem
            return
        
        mid = (start + end) // 2
        self.build(2 * node, start, mid)
        self.build(2 * node + 1, mid + 1, end)
        
        l_rem, l_prod = self.tree_remain[2 * node], self.tree_prod[2 * node]
        r_rem, r_prod = self.tree_remain[2 * node + 1], self.tree_prod[2 * node + 1]
        self.tree_remain[node], self.tree_prod[node] = self._combine(l_rem, l_prod, r_rem, r_prod)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.nums[idx] = val
            rem = val % self.k
            self.tree_remain[node] = [0] * self.k
            self.tree_remain[node][rem] = 1
            self.tree_prod[node] = rem
            return
        
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
            
        l_rem, l_prod = self.tree_remain[2 * node], self.tree_prod[2 * node]
        r_rem, r_prod = self.tree_remain[2 * node + 1], self.tree_prod[2 * node + 1]
        self.tree_remain[node], self.tree_prod[node] = self._combine(l_rem, l_prod, r_rem, r_prod)

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return None, 1
        if l <= start and end <= r:
            return self.tree_remain[node], self.tree_prod[node]
        
        mid = (start + end) // 2
        left_rem, left_prod = self.query(2 * node, start, mid, l, r)
        right_rem, right_prod = self.query(2 * node + 1, mid + 1, end, l, r)
        
        if left_rem is None:
            return right_rem, right_prod
        if right_rem is None:
            return left_rem, left_prod
            
        return self._combine(left_rem, left_prod, right_rem, right_prod)

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg_tree = SegmentTree(nums, k)
        result = []
        
        for idx, val, start, x in queries:
            # Step 1: Update nums[idx] to val
            seg_tree.update(1, 0, n - 1, idx, val)
            
            # Step 2: Query the range [start, n - 1]
            freq, _ = seg_tree.query(1, 0, n - 1, start, n - 1)
            
            # Step 3: Get the answer for remainder x
            ans = freq[x] if freq else 0
            result.append(ans)
            
        return result