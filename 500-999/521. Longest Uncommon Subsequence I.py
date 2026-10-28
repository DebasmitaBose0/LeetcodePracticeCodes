class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # If strings are identical, there is no uncommon subsequence
        if a == b:
            return -1
        
        # Otherwise, the longer string itself is the longest uncommon subsequence
        return max(len(a), len(b))