from bisect import insort

class SummaryRanges:
    def __init__(self):
        # Using a sorted list to keep track of unique numbers
        self.nums = []
        self.seen = set()

    def addNum(self, value: int) -> None:
        if value not in self.seen:
            self.seen.add(value)
            # Maintain sorted order: O(N)
            insort(self.nums, value)

    def getIntervals(self) -> List[List[int]]:
        if not self.nums:
            return []
        
        intervals = []
        start = end = self.nums[0]
        
        for i in range(1, len(self.nums)):
            curr = self.nums[i]
            # Check if the current number continues the existing interval
            if curr == end + 1:
                end = curr
            else:
                # Close the current interval and start a new one
                intervals.append([start, end])
                start = end = curr
        
        # Append the final interval
        intervals.append([start, end])
        return intervals