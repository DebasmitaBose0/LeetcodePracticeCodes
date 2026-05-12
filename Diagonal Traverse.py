class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        # There are (m + n - 1) total diagonals
        for d in range(m + n - 1):
            # Temporary list to store elements of the current diagonal
            diagonal = []
            
            # Determine starting point of the diagonal
            # For sum 'd', row 'i' starts at d if d < m, else it starts at m-1
            # Column 'j' is then d - i
            r = d if d < m else m - 1
            c = d - r
            
            # Traverse until we go out of bounds
            while r >= 0 and c < n:
                diagonal.append(mat[r][c])
                r -= 1
                c += 1
            
            # If the diagonal index is odd, we need to reverse it to go "down"
            if d % 2 == 1:
                result.extend(diagonal[::-1])
            else:
                result.extend(diagonal)
                
        return result