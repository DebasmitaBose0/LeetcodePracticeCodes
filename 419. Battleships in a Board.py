class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        
        count = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    # Check if there is an 'X' above or to the left
                    # If so, this is part of a ship we already counted
                    if (r > 0 and board[r-1][c] == 'X') or \
                       (c > 0 and board[r][c-1] == 'X'):
                        continue
                    count += 1
        return count