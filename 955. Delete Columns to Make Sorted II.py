class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        # is_sorted[i] means strs[i] < strs[i+1] is already guaranteed
        is_sorted = [False] * (n - 1)
        res = 0
        
        for j in range(m):
            is_valid_column = True
            for i in range(n - 1):
                # If row pair i, i+1 is not yet sorted and this char breaks order
                if not is_sorted[i] and strs[i][j] > strs[i+1][j]:
                    is_valid_column = False
                    break
            
            if is_valid_column:
                # Keep the column and update which rows are now guaranteed sorted
                for i in range(n - 1):
                    if strs[i][j] < strs[i+1][j]:
                        is_sorted[i] = True
            else:
                # Must delete this column
                res += 1
                
        return res