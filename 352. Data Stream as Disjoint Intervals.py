import bisect

class SummaryRanges:

    def __init__(self):
        # We store intervals as [start, end]
        self.intervals = []

    def addNum(self, value: int) -> None:
        # Find where [value, value] would be inserted to maintain sort order
        idx = bisect.bisect_left(self.intervals, [value, value])
        
        # --- FIXED DUPLICATE CHECK ---
        # Check if value is already covered by the interval at idx-1
        if idx > 0 and self.intervals[idx-1][0] <= value <= self.intervals[idx-1][1]:
            return
        # Check if value is already covered by the interval at idx
        if idx < len(self.intervals) and self.intervals[idx][0] <= value <= self.intervals[idx][1]:
            return
        # -----------------------------

        # Determine if we should merge with neighbors
        merge_prev = (idx > 0 and self.intervals[idx-1][1] + 1 == value)
        merge_next = (idx < len(self.intervals) and self.intervals[idx][0] - 1 == value)
        
        if merge_prev and merge_next:
            # Connects two intervals: [start, val-1] + [val] + [val+1, end]
            self.intervals[idx-1][1] = self.intervals[idx][1]
            self.intervals.pop(idx)
        elif merge_prev:
            # Extend previous: [start, val-1] -> [start, val]
            self.intervals[idx-1][1] = value
        elif merge_next:
            # Extend next: [val+1, end] -> [val, end]
            self.intervals[idx][0] = value
        else:
            # Insert a new disjoint interval
            self.intervals.insert(idx, [value, value])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals