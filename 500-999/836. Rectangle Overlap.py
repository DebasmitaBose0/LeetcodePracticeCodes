from ast import List
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Check if they DO NOT overlap
        is_not_overlapping = (
            rec1[2] <= rec2[0] or  # rec1 is to the left of rec2
            rec1[0] >= rec2[2] or  # rec1 is to the right of rec2
            rec1[3] <= rec2[1] or  # rec1 is below rec2
            rec1[1] >= rec2[3]     # rec1 is above rec2
        )
        
        # If they don't not overlap, they overlap!
        return not is_not_overlapping