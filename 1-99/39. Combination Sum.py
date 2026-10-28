class Solution:
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(start, path, remaining):
            # Base case
            if remaining == 0:
                result.append(path[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Choose
                path.append(candidates[i])
                
                # Stay at same index (reuse allowed)
                backtrack(i, path, remaining - candidates[i])
                
                # Undo (backtrack)
                path.pop()
        
        backtrack(0, [], target)
        return result