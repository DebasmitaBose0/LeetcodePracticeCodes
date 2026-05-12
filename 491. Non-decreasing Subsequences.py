class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start, path):
            # If the current path has at least 2 elements, it's a valid subsequence
            if len(path) > 1:
                res.append(list(path))
            
            # Use a set to prevent processing the same number at the same recursion level
            # This handles duplicate elements in the input array
            used = set()
            
            for i in range(start, len(nums)):
                # 1. Skip if the number was already used at this level
                # 2. Skip if it's not non-decreasing
                if nums[i] in used or (path and nums[i] < path[-1]):
                    continue
                
                used.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop() # Backtrack step
        
        backtrack(0, [])
        return res