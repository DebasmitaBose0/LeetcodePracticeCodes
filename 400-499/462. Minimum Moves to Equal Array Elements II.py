class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # 1. Sort the array to find the median
        nums.sort()
        
        # 2. Identify the median (middle element)
        median = nums[len(nums) // 2]
        
        # 3. Calculate total moves to bring every element to the median
        total_moves = 0
        for num in nums:
            total_moves += abs(num - median)
            
        return total_moves