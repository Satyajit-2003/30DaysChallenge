from typing import List

# The colloision doesn't affect anything, it is like the ant passes each other
# So we have to find the farthest ant from either end and take the max of both

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left_time = max(left) if left else 0
        right_time = (n - min(right) ) if right else 0
        return max(left_time, right_time)