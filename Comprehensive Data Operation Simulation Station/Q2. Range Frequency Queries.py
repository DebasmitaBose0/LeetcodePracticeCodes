import bisect
from collections import defaultdict

class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        # Map each value to a list of its indices in sorted order
        self.indices_map = defaultdict(list)
        for i, val in enumerate(arr):
            self.indices_map[val].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.indices_map:
            return 0
        
        indices = self.indices_map[value]
        
        # Find the range of indices that fall within [left, right]
        # binary search for the first index >= left
        start_pos = bisect.bisect_left(indices, left)
        # binary search for the first index > right
        end_pos = bisect.bisect_right(indices, right)
        
        # The number of elements in the range [start_pos, end_pos)
        return end_pos - start_pos