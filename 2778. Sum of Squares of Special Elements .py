from ast import List
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        # Iterate through the 1-indexed array from 1 to n
        for i in range(1, n + 1):
            if n % i == 0:
                # Add the square of the element (adjusting index for 0-indexed Python array: i - 1)
                total_sum += nums[i - 1] ** 2
                
        return total_sum