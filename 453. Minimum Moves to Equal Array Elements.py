class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Find the minimum element in the array
        min_val = min(nums)
        
        # Calculate the total moves based on the simplified formula
        total_moves = 0
        for num in nums:
            total_moves += num - min_val
            
        return total_moves