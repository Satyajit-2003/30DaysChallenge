# Find the nearest point on the rectangle to the center of the circle
# If the distance between the nearest point and the center of the circle is less than or equal to the radius of the circle, then the circle and the rectangle overlap

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearest_x = max(x1, min(x2, xCenter))
        nearest_y = max(y1, min(y2, yCenter))

        dist = ((nearest_x - xCenter)**2) + ((nearest_y - yCenter)**2)

        if dist <= radius**2:
            return True
        return False