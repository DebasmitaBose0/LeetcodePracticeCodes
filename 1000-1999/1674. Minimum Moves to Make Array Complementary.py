class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # diff[i] tracks the change in moves for a target sum of i
        diff = [0] * (2 * limit + 2)
        n = len(nums)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            # Range for 2 moves: [2, 2*limit]
            # We start by adding 2 to everything (conceptually)
            diff[2] += 2
            
            # Range for 1 move: [min(a,b)+1, max(a,b)+limit]
            # In this range, we only need 1 move, so we subtract 1 from the "2 moves"
            diff[min(a, b) + 1] -= 1
            diff[max(a, b) + limit + 1] += 1
            
            # Range for 0 moves: sum is exactly a + b
            # We subtract another 1 at this specific point
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            
        res = n
        curr_moves = 0
        # Sweep through the difference array to find the minimum
        for i in range(2, 2 * limit + 1):
            curr_moves += diff[i]
            res = min(res, curr_moves)
            
        return res