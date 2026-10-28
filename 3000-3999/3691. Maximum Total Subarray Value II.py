import math

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0 or k == 0:
            return 0
            
        # 1. Build Sparse Tables for O(1) Range Max and Range Min queries
        max_power = int(math.log2(n)) + 1
        st_max = [[0] * max_power for _ in range(n)]
        st_min = [[0] * max_power for _ in range(n)]
        
        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]
            
        for j in range(1, max_power):
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j-1], st_max[i + (1 << (j-1))][j-1])
                st_min[i][j] = min(st_min[i][j-1], st_min[i + (1 << (j-1))][j-1])
                
        def get_val(l: int, r: int) -> int:
            if l > r:
                return 0
            j = int(math.log2(r - l + 1))
            mx = max(st_max[l][j], st_max[r - (1 << j) + 1][j])
            mn = min(st_min[l][j], st_min[r - (1 << j) + 1][j])
            return mx - mn

        # 2. Max-Heap Initialization
        # Python's heapq is a min-heap, so we store negative values to simulate a max-heap
        import heapq
        heap = []
        
        for l in range(n):
            val = get_val(l, n - 1)
            # Push format: (-value, left_index, right_index)
            heapq.heappush(heap, (-val, l, n - 1))
            
        # 3. Extract the top K elements
        total_value = 0
        for _ in range(k):
            if not heap:
                break
            neg_val, l, r = heapq.heappop(heap)
            total_value += -neg_val
            
            # If there's a smaller valid subarray starting at l, push it
            if r > l:
                next_r = r - 1
                next_val = get_val(l, next_r)
                heapq.heappush(heap, (-next_val, l, next_r))
                
        return total_value