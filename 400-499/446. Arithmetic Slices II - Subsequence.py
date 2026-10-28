from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_count = 0
        # dp[i][diff] stores the number of arithmetic subsequences 
        # ending at index i with common difference 'diff'
        dp = [defaultdict(int) for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                # Number of arithmetic subsequences ending at j with 'diff'
                count_at_j = dp[j][diff]
                
                # These sequences extended to i form sequences of length >= 3
                total_count += count_at_j
                
                # Update dp[i][diff]: 
                # count_at_j: existing sequences of length >= 2 extended to i
                # + 1: the new pair (nums[j], nums[i]) which is length 2
                dp[i][diff] += count_at_j + 1
                
        return total_count