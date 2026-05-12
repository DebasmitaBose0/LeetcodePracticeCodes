class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # Define the corners of the bounding box
        x1, y1 = float('inf'), float('inf')
        x2, y2 = float('-inf'), float('-inf')
        
        points = set()
        total_area = 0
        
        for rect in rectangles:
            # Update overall bounding box coordinates
            x1, y1 = min(x1, rect[0]), min(y1, rect[1])
            x2, y2 = max(x2, rect[2]), max(y2, rect[3])
            
            # Add area of current rectangle
            total_area += (rect[2] - rect[0]) * (rect[3] - rect[1])
            
            # Identify the four corners of the current small rectangle
            curr_corners = [
                (rect[0], rect[1]), (rect[0], rect[3]),
                (rect[2], rect[1]), (rect[2], rect[3])
            ]
            
            # For each corner, if it's already in the set, remove it (even count)
            # If it's not in the set, add it (odd count)
            for p in curr_corners:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)
        
        # Rule 1: Area check
        if total_area != (x2 - x1) * (y2 - y1):
            return False
        
        # Rule 2: Vertex check
        # The set should contain exactly the 4 corners of the large bounding box
        if len(points) != 4 or \
           (x1, y1) not in points or (x1, y2) not in points or \
           (x2, y1) not in points or (x2, y2) not in points:
            return False
            
        return True