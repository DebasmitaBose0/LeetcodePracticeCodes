class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start ascending, then by end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        max_end = 0
        
        for start, end in intervals:
            # If the current interval's end is past the max_end seen so far,
            # it is not covered.
            if end > max_end:
                count += 1
                max_end = end
                
        return count