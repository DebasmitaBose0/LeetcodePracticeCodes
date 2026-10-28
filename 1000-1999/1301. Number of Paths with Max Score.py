from ast import List
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        
        # dp[r][c] will store [max_score, path_count]
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        # Base case: Starting at 'E' (0, 0)
        dp[0][0] = [0, 1]
        
        for r in range(n):
            for c in range(n):
                # Skip the starting point (already initialized) and obstacles
                if (r == 0 and c == 0) or board[r][c] == 'X':
                    continue
                
                max_score = -1
                path_count = 0
                
                # Check the three potential predecessors: up, left, up-left diagonal
                for dr, dc in [(-1, 0), (0, -1), (-1, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and dp[nr][nc][0] != -1:
                        prev_score, prev_count = dp[nr][nc]
                        if prev_score > max_score:
                            max_score = prev_score
                            path_count = prev_count
                        elif prev_score == max_score:
                            path_count = (path_count + prev_count) % MOD
                
                # If a valid path reaches this cell, add its current value
                if max_score != -1:
                    current_val = 0
                    if board[r][c].isdigit():
                        current_val = int(board[r][c])
                    dp[r][c] = [max_score + current_val, path_count]
                    
        # The answer will be accumulated at 'S' (n-1, n-1)
        res_score, res_count = dp[n-1][n-1]
        return [res_score if res_score != -1 else 0, res_count]