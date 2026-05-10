class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the 2D grid into a 1D list
        nums = []
        for row in grid:
            nums.extend(row)
        
        # Sort the numbers to find the median
        nums.sort()
        
        # Check if it's even possible to make all values equal
        # All elements must have the same remainder when divided by x
        mod = nums[0] % x
        for num in nums:
            if num % x != mod:
                return -1
        
        # The median is the optimal target value
        median = nums[len(nums) // 2]
        
        operations = 0
        for num in nums:
            # Calculate the number of steps of 'x' needed to reach the median
            operations += abs(num - median) // x
            
        return operations