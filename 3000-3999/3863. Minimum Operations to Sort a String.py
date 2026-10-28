class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        # 0 operations: already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
        
        # Proper substrings of length <= 2 cannot fix an unsorted string
        if n <= 2:
            return -1
        
        min_char = min(s)
        max_char = max(s)
        
        # 1 operation: min at index 0 or max at index n - 1
        if s[0] == min_char or s[-1] == max_char:
            return 1
        
        # 3 operations only if:
        # 1) The ONLY occurrences of min_char are at index n - 1 (meaning none in s[:n-1])
        # AND
        # 2) The ONLY occurrences of max_char are at index 0 (meaning none in s[1:])
        has_min_before_end = min_char in s[:-1]
        has_max_after_start = max_char in s[1:]
        
        if not has_min_before_end and not has_max_after_start:
            return 3
        
        # Otherwise, 2 operations are always enough
        return 2