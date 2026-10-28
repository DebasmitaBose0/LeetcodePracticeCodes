import collections
import re

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # Helper to handle the "chain reaction" of clearing balls
        def clean(s):
            n = len(s)
            res = ""
            i = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                if j - i < 3:
                    res += s[i:j]
                i = j
            return clean(res) if len(res) != n else res

        # Initial state: (current_board, sorted_hand)
        hand = "".join(sorted(hand))
        queue = collections.deque([(board, hand, 0)])
        visited = set([(board, hand)])

        while queue:
            curr_board, curr_hand, steps = queue.popleft()
            
            if not curr_board:
                return steps
            
            # Try inserting each ball in the hand into every possible position
            for i in range(len(curr_hand)):
                # Skip duplicate balls in hand to prune search
                if i > 0 and curr_hand[i] == curr_hand[i-1]:
                    continue
                
                for j in range(len(curr_board) + 1):
                    # Optimization: Only insert if it makes sense
                    # 1. Same color as current ball (to build a group)
                    # 2. Between two different colors (to potentially bridge them later)
                    new_board = clean(curr_board[:j] + curr_hand[i] + curr_board[j:])
                    new_hand = curr_hand[:i] + curr_hand[i+1:]
                    
                    if not new_board:
                        return steps + 1
                    
                    if (new_board, new_hand) not in visited:
                        visited.add((new_board, new_hand))
                        queue.append((new_board, new_hand, steps + 1))
        
        return -1