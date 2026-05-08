import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 1. Sort width in ascending order.
        # 2. If widths are equal, sort height in DESCENDING order.
        # This prevents picking two envelopes with the same width.
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # 3. Find the LIS of the heights
        lis = []
        for _, h in envelopes:
            # Find the leftmost insertion point to maintain sorted order
            idx = bisect.bisect_left(lis, h)
            
            # If idx is equal to the length of lis, h is the largest height found
            if idx == len(lis):
                lis.append(h)
            else:
                # Replace the existing element at idx with h
                # This keeps the possible heights as small as possible
                lis[idx] = h
                
        return len(lis)