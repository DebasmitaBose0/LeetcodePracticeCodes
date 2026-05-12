class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Number of rows (n) and number of columns (length of strings)
        rows = len(strs)
        cols = len(strs[0])
        
        delete_count = 0
        
        # Check each column one by one
        for j in range(cols):
            for i in range(1, rows):
                # Compare current character with the one in the row above
                if strs[i][j] < strs[i-1][j]:
                    # Not sorted, increment count and stop checking this column
                    delete_count += 1
                    break
                    
        return delete_count