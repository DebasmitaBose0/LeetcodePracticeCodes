class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 1. Convert all timePoints to minutes
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            minutes.append(h * 60 + m)
            
        # 2. Sort the minutes
        minutes.sort()
        
        # 3. Find the minimum difference between adjacent times
        min_diff = float('inf')
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
            
        # 4. Handle the circular case (last time vs first time of next day)
        # Total minutes in a day = 24 * 60 = 1440
        circular_diff = (1440 - minutes[-1]) + minutes[0]
        min_diff = min(min_diff, circular_diff)
        
        return min_diff