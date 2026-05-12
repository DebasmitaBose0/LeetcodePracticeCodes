class Solution:
    def findRotation(self, mat, target):
        
        def rotate(matrix):
            # Transpose
            for i in range(len(matrix)):
                for j in range(i, len(matrix)):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            # Reverse each row
            for row in matrix:
                row.reverse()
        
        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
        
        return False