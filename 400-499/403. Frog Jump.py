class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Use a set for O(1) lookups of stone positions
        stone_set = set(stones)
        target = stones[-1]
        memo = {}

        def solve(curr, k):
            # If we reached the last stone
            if curr == target:
                return True
            # Check memo to avoid redundant calculations
            if (curr, k) in memo:
                return memo[(curr, k)]
            
            # Try the three possible jump distances
            for jump in (k - 1, k, k + 1):
                if jump > 0: # Frog can only move forward
                    next_stone = curr + jump
                    if next_stone in stone_set:
                        if solve(next_stone, jump):
                            memo[(curr, k)] = True
                            return True
            
            memo[(curr, k)] = False
            return False

        # First jump must be exactly 1 unit from the first stone (stones[0] is always 0)
        # However, the problem says the first jump is 1, so we start at stone 1 
        # (if it exists) with a last jump of 1.
        if stones[1] != 1:
            return False
            
        return solve(1, 1)