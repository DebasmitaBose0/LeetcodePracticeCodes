class Solution:
    def countSegments(self, s: str) -> int:
        # split() without arguments handles multiple spaces and leading/trailing spaces
        return len(s.split())