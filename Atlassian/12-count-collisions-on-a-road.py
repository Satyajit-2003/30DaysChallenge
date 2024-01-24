# All cars going left on left wont collide
# All cars going right on right wont collide
# All other cars will collide
# For LR and RL collisions, we have 2 points
# For LS and RS collisions, we have 1 point
# So remaining all cars will contribute to the collision count with 1 point except for stationary cars


class Solution:
    def countCollisions(self, directions: str) -> int:
        return len(directions.lstrip('L').rstrip('R')) - directions.count('S')