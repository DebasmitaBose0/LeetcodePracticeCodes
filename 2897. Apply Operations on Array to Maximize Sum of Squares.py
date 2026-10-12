from typing import List

class Solution:
    def maxSumSquares(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 32
        
        for num in nums:
            for bit in range(32):
                if (num >> bit) & 1:
                    count[bit] += 1
                    
        total_sum = 0
        for _ in range(k):
            val = 0
            for bit in range(32):
                if count[bit] > 0:
                    val |= (1 << bit)
                    count[bit] -= 1
            total_sum = (total_sum + val * val) % MOD
            
        return total_sum
