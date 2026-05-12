class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # Sort by length descending to find the longest one first
        strs.sort(key=len, reverse=True)
        
        def isSubsequence(s1: str, s2: str) -> bool:
            # Standard two-pointer check
            i = 0
            for char in s2:
                if i < len(s1) and s1[i] == char:
                    i += 1
            return i == len(s1)
        
        for i, s1 in enumerate(strs):
            is_uncommon = True
            for j, s2 in enumerate(strs):
                if i == j:
                    continue
                if isSubsequence(s1, s2):
                    is_uncommon = False
                    break
            
            if is_uncommon:
                return len(s1)
        
        return -1