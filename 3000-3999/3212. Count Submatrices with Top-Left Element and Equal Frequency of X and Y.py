class Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        
        # prefix sum and X count
        prefix_sum = [[0]*n for _ in range(m)]
        prefix_X = [[0]*n for _ in range(m)]
        
        def val(c):
            if c == 'X':
                return 1
            elif c == 'Y':
                return -1
            return 0
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                current = val(grid[i][j])
                x_val = 1 if grid[i][j] == 'X' else 0
                
                top = prefix_sum[i-1][j] if i > 0 else 0
                left = prefix_sum[i][j-1] if j > 0 else 0
                diag = prefix_sum[i-1][j-1] if i > 0 and j > 0 else 0
                
                prefix_sum[i][j] = current + top + left - diag
                
                # same for X count
                topX = prefix_X[i-1][j] if i > 0 else 0
                leftX = prefix_X[i][j-1] if j > 0 else 0
                diagX = prefix_X[i-1][j-1] if i > 0 and j > 0 else 0
                
                prefix_X[i][j] = x_val + topX + leftX - diagX
                
                # check conditions
                if prefix_sum[i][j] == 0 and prefix_X[i][j] > 0:
                    count += 1
        
        return count