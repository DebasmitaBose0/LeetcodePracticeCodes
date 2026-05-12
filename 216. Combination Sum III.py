class Solution:
    def combinationSum3(self, k, n):
        result = []
        
        def backtrack(start, path, total):
            # valid combination
            if len(path) == k and total == n:
                result.append(path[:])
                return
            
            # pruning
            if len(path) > k or total > n:
                return
            
            for i in range(start, 10):  # numbers 1 to 9
                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()
        
        backtrack(1, [], 0)
        return result