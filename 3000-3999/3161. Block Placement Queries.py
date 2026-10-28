import bisect

class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * size)

    def update(self, index, value, node, start, end):
        if start == end:
            self.tree[node] = value
            return
        mid = (start + end) // 2
        if index <= mid:
            self.update(index, value, 2 * node, start, mid)
        else:
            self.update(index, value, 2 * node + 1, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, l, r, node, start, end):
        if r < start or l > end or l > r:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(l, r, 2 * node, start, mid)
        p2 = self.query(l, r, 2 * node + 1, mid + 1, end)
        return max(p1, p2)

class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        # Determine max coordinate limit dynamically up to 50000
        max_x = 0
        for q in queries:
            max_x = max(max_x, q[1])
        
        M = max_x + 2
        seg_tree = SegmentTree(M)
        
        # Track obstacles in a sorted list. Initially, we have boundaries at 0 and a virtual infinity.
        # Using a large number safely beyond max_x acting as the rightmost boundary.
        obstacles = [0, M] 
        
        results = []
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                # Find where x fits among existing obstacles
                idx = bisect.bisect_left(obstacles, x)
                L = obstacles[idx - 1]
                R = obstacles[idx]
                
                # Insert x into sorted obstacles
                obstacles.insert(idx, x)
                
                # Update segment tree with new split distances
                seg_tree.update(x, x - L, 1, 0, M - 1)
                seg_tree.update(R, R - x, 1, 0, M - 1)
                
            elif q[0] == 2:
                x, sz = q[1], q[2]
                
                # Find the closest obstacle to the left of or equal to x
                idx = bisect.bisect_right(obstacles, x)
                L = obstacles[idx - 1]
                
                # 1. Max gap completely captured between obstacles up to L
                max_gap_before_L = seg_tree.query(0, L, 1, 0, M - 1)
                
                # 2. Trailing space gap between the last obstacle L and target point x
                trailing_gap = x - L
                
                max_available = max(max_gap_before_L, trailing_gap)
                
                results.append(max_available >= sz)
                
        return results