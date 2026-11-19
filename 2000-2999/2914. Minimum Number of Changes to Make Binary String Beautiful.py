class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        # Iterate through the string by stepping 2 characters at a time
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                changes += 1
        return changes  