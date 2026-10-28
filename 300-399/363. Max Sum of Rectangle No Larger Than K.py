import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = float('-inf')
        
        # Optimization: Ensure we iterate over the smaller dimension
        # If rows > cols, we fix left/right columns; otherwise fix top/bottom rows.
        for l in range(cols):
            row_sums = [0] * rows
            for r in range(l, cols):
                for i in range(rows):
                    row_sums[i] += matrix[i][r]
                
                # Now solve the 1D problem: Find max subarray sum <= k
                # We use a sorted list of prefix sums to perform binary search
                sorted_sums = [0]
                current_sum = 0
                for s in row_sums:
                    current_sum += s
                    # We want: current_sum - prev_sum <= k  =>  prev_sum >= current_sum - k
                    idx = bisect.bisect_left(sorted_sums, current_sum - k)
                    
                    if idx < len(sorted_sums):
                        res = max(res, current_sum - sorted_sums[idx])
                    
                    # Optimization: If we hit k exactly, we can't do better
                    if res == k: return k
                    
                    bisect.insort(sorted_sums, current_sum)
                    
        return res