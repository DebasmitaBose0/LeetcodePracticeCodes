class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Helper function to check if a capacity is feasible
        def can_split(capacity):
            subarray_count = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > capacity:
                    # Start a new subarray
                    subarray_count += 1
                    current_sum = num
                    if subarray_count > k:
                        return False
                else:
                    current_sum += num
            return True

        # Binary search range
        left = max(nums)
        right = sum(nums)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            if can_split(mid):
                ans = mid
                right = mid - 1 # Try to find a smaller "largest sum"
            else:
                left = mid + 1 # Need a larger capacity
                
        return ans