class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        
        # Step 1: Precompute prefix minimums
        left_min = [0] * n
        curr_min = nums[0]
        for i in range(1, n):
            left_min[i] = curr_min
            curr_min = min(curr_min, nums[i])
            
        # Step 2: Precompute suffix minimums
        right_min = [0] * n
        curr_min = nums[-1]
        for i in range(n - 2, -1, -1):
            right_min[i] = curr_min
            curr_min = min(curr_min, nums[i])
            
        # Step 3: Iterate and find the minimum mountain sum
        min_total_sum = float('inf')
        found = False
        
        for j in range(1, n - 1):
            # Check the mountain condition
            if left_min[j] < nums[j] > right_min[j]:
                found = True
                current_sum = left_min[j] + nums[j] + right_min[j]
                min_total_sum = min(min_total_sum, current_sum)
                
        return min_total_sum if found else -1