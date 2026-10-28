class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        res = float('inf') # Fix 1: Correct infinity initialization
        
        for i in range(n):
            if words[i] == target:
                d = abs(i - startIndex)
                # Fix 2: Standard circular distance logic
                res = min(res, d, n - d)
        
        # Fix 3: Return -1 if the target was never found
        return res if res != float('inf') else -1