import bisect

class RangeModule:

    def __init__(self):
        self.tracks = []

    def addRange(self, left: int, right: int) -> None:
        # Find where left and right would fit in the sorted list
        i = bisect.bisect_left(self.tracks, left)
        j = bisect.bisect_right(self.tracks, right)
        
        sub = []
        # If i is even, 'left' is outside an existing range, so it's a new start
        if i % 2 == 0:
            sub.append(left)
        # If j is even, 'right' is outside an existing range, so it's a new end
        if j % 2 == 0:
            sub.append(right)
            
        # Replace everything between i and j with our new boundaries
        self.tracks[i:j] = sub

    def queryRange(self, left: int, right: int) -> bool:
        # Find the insertion point for left and right
        i = bisect.bisect_right(self.tracks, left)
        j = bisect.bisect_left(self.tracks, right)
        
        # Every number is tracked if:
        # 1. 'left' is inside a range (i is odd)
        # 2. 'left' and 'right' are within the same range (i == j)
        return i % 2 == 1 and i == j

    def removeRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.tracks, left)
        j = bisect.bisect_right(self.tracks, right)
        
        sub = []
        # If i is odd, 'left' is inside a range, so it becomes a new end
        if i % 2 == 1:
            sub.append(left)
        # If j is odd, 'right' is inside a range, so it becomes a new start
        if j % 2 == 1:
            sub.append(right)
            
        self.tracks[i:j] = sub