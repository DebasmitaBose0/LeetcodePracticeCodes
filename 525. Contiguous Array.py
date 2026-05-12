class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Map to store {current_sum: first_index}
        sum_map = {0: -1}
        max_length = 0
        current_sum = 0
        
        for i, num in enumerate(nums):
            # Treat 0 as -1, and 1 as 1
            current_sum += 1 if num == 1 else -1
            
            if current_sum in sum_map:
                # Calculate length from the first time we saw this sum to now
                max_length = max(max_length, i - sum_map[current_sum])
            else:
                # Only store the first occurrence to keep the subarray as long as possible
                sum_map[current_sum] = i
                
        return max_length