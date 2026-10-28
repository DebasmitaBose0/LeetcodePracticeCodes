import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # 1. Create a list of [start_point, original_index]
        starts = []
        for i in range(len(intervals)):
            starts.append([intervals[i][0], i])
        
        # 2. Sort the list by start_point
        starts.sort()
        
        # Extract just the sorted start points for binary search
        sorted_start_points = [item[0] for item in starts]
        
        res = []
        
        # 3. For each interval, find the 'right interval'
        for i in range(len(intervals)):
            target = intervals[i][1] # We need start_j >= end_i
            
            # Use binary search to find the smallest start_point >= target
            idx = bisect.bisect_left(sorted_start_points, target)
            
            if idx < len(starts):
                # If found, append the original index stored in starts[idx]
                res.append(starts[idx][1])
            else:
                # No such interval exists
                res.append(-1)
                
        return res