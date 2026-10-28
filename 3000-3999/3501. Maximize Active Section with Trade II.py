from typing import List
import math
import bisect

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # Total ones in the whole string s
        total_ones = s.count('1')
        
        # Extract zero segments
        zeros = [] # (start_idx, end_idx, length)
        i = 0
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                zeros.append((i, j - 1, j - i))
                i = j
            else:
                i += 1
                
        num_zeros = len(zeros)
        
        # Precalculate Sparse Table for adjacent zero segment length sums
        if num_zeros >= 2:
            arr = [zeros[i][2] + zeros[i + 1][2] for i in range(num_zeros - 1)]
            m = len(arr)
            K = int(math.log2(m)) + 1 if m > 0 else 1
            st = [[0] * K for _ in range(m)]
            
            for i in range(m):
                st[i][0] = arr[i]
                
            for j in range(1, K):
                length = 1 << (j - 1)
                for i in range(m - (1 << j) + 1):
                    st[i][j] = max(st[i][j - 1], st[i + length][j - 1])
                    
            def query_st(L: int, R: int) -> int:
                if L > R:
                    return 0
                j = int(math.log2(R - L + 1))
                return max(st[L][j], st[R - (1 << j) + 1][j])
        else:
            def query_st(L: int, R: int) -> int:
                return 0

        zero_starts = [z[0] for z in zeros]
        zero_ends = [z[1] for z in zeros]

        ans = []
        for l, r in queries:
            # Overlapping zero segments with [l, r]
            first_z = bisect.bisect_left(zero_ends, l)
            last_z = bisect.bisect_right(zero_starts, r) - 1
            
            # Need at least 2 zero segments in [l, r] to have an internal 1-block surrounded by 0s
            if last_z - first_z < 1:
                ans.append(total_ones)
                continue
                
            eff_len = {}
            for z_idx in range(first_z, last_z + 1):
                st_i, en_i, _ = zeros[z_idx]
                eff_len[z_idx] = min(en_i, r) - max(st_i, l) + 1
                
            max_gain = 0
            
            # 1. Internal pairs (fully unclipped by range boundaries)
            if last_z - 1 >= first_z + 1:
                internal_max = query_st(first_z + 1, last_z - 2)
                max_gain = max(max_gain, internal_max)
                
            # 2. Boundary-adjacent pairs
            for z_idx in range(first_z, last_z):
                gain = eff_len[z_idx] + eff_len[z_idx + 1]
                max_gain = max(max_gain, gain)
                
            ans.append(total_ones + max_gain)
            
        return ans