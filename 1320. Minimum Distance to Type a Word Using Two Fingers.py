from functools import cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        
        # Helper to get (row, col) for a character
        def get_pos(char):
            idx = ord(char) - ord('A')
            return divmod(idx, 6) # Returns (row, col)

        @cache
        def dp(index, f1, f2):
            # Base case: all characters typed
            if index == len(word):
                return 0
            
            target_pos = get_pos(word[index])
            
            # Option 1: Move Finger 1
            cost1 = 0
            if f1 is not None:
                cost1 = abs(f1[0] - target_pos[0]) + abs(f1[1] - target_pos[1])
            res1 = cost1 + dp(index + 1, target_pos, f2)
            
            # Option 2: Move Finger 2
            cost2 = 0
            if f2 is not None:
                cost2 = abs(f2[0] - target_pos[0]) + abs(f2[1] - target_pos[1])
            res2 = cost2 + dp(index + 1, f1, target_pos)
            
            return min(res1, res2)

        # Initial call: index 0, both fingers have no position (None)
        return dp(0, None, None)