from math import gcd

class Solution:
    def minOperations(self, nums):
        n = len(nums)
        ones = nums.count(1)
        
        if ones:
            return n - ones
        
        ans = float('inf')
        
        for i in range(n):
            g = nums[i]
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    ans = min(ans, j - i)
                    break
        
        return ans + n - 1 if ans != float('inf') else -1