class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        # If the total number of elements doesn't match, return original
        if m * n != r * c:
            return mat
        
        # Initialize the new matrix with zeros
        result = [[0] * c for _ in range(r)]
        
        # Fill the new matrix
        for i in range(m * n):
            # i // n, i % n gives original row/col
            # i // c, i % c gives new row/col
            result[i // c][i % c] = mat[i // n][i % n]
            
        return result