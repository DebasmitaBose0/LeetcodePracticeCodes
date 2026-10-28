class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        # Base case for length 1 (though constraints say n >= 3)
        if n == 1:
            return m
            
        size = 2 * m
        
        # Helper function to multiply two matrices under MOD
        def multiply(matA, matB):
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if matA[i][k] == 0:
                        continue
                    for j in range(size):
                        res[i][j] = (res[i][j] + matA[i][k] * matB[k][j]) % MOD
            return res

        # Helper function for fast matrix exponentiation
        def power(mat, p):
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                res[i][i] = 1  # Identity matrix
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, mat)
                mat = multiply(mat, mat)
                p //= 2
            return res

        # Build the transition matrix T
        T = [[0] * size for _ in range(size)]
        
        # Indices 0 to m-1: Down states
        # Indices m to 2m-1: Up states
        for x in range(m):
            # From Down state x, we can go to Up state y if y < x
            for y in range(x):
                T[x][m + y] = 1
            
            # From Up state x, we can go to Down state y if y > x
            for y in range(x + 1, m):
                T[m + x][y] = 1

        # Compute T^(n-1)
        T_pow = power(T, n - 1)
        
        # Initial state vector: for n=1, any element can start as a peak or a valley
        # We can simulate this by summing up transitions starting from all possible base positions
        total_valid = 0
        for i in range(size):
            for j in range(size):
                total_valid = (total_valid + T_pow[i][j]) % MOD
                
        return total_valid