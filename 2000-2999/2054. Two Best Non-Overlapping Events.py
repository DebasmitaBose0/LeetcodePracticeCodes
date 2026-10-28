import bisect

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # 1. Sort events by startTime
        events.sort()
        n = len(events)
        
        # 2. Create a suffix max array
        # suffix_max[i] = max value of events from index i to n-1
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], events[i][2])
            
        max_sum = 0
        
        # 3. For each event, find the best non-overlapping event that starts after it ends
        for start, end, value in events:
            # Update max_sum with the current event alone
            max_sum = max(max_sum, value)
            
            # Find the first event that starts > end
            # We look for the index where startTime >= end + 1
            idx = bisect.bisect_right(events, [end, float('inf'), float('inf')])
            
            if idx < n:
                max_sum = max(max_sum, value + suffix_max[idx])
                
        return max_sum