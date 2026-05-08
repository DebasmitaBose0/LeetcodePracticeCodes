class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        # Calculate F(0)
        current_f = sum(i * val for i, val in enumerate(nums))
        max_f = current_f
        
        # Iteratively calculate F(1) to F(n-1) using the formula
        for k in range(1, n):
            # F(k) = F(k-1) + total_sum - n * nums[n-k]
            current_f = current_f + total_sum - n * nums[n-k]
            if current_f > max_f:
                max_f = current_f
                
        return max_f