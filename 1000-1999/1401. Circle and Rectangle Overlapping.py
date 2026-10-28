class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        # Find the closest point on the rectangle to the circle's center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))

        # Calculate the squared distance from the circle center to this closest point
        dx = xCenter - closest_x
        dy = yCenter - closest_y
        distance_sq = dx * dx + dy * dy

        # Check if the distance is less than or equal to the squared radius
        return distance_sq <= radius * radius