class Solution:
    def checkRecord(self, s: str) -> bool:
        # Criterion 1: Fewer than 2 absences total
        # Criterion 2: No 3 or more consecutive late days
        return s.count('A') < 2 and "LLL" not in s