class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If lengths are different, s can never become goal
        if len(s) != len(goal):
            return False
        
        # Check if goal is a substring of s + s
        return goal in (s + s)