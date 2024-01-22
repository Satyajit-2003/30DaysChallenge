from typing import List

# Sort the bars and find the maximum gap between two consecutive bars.
# The answer is the minimum of the maximum gap in horizontal and vertical bars.
# Add 2 to the answer to account for the bars at the edges.

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        max_h = max_v = 0

        t = 0
        for i in range(1, len(hBars)):
            if hBars[i-1] + 1 != hBars[i]:
                max_h = max(t, max_h)
                t = 0
            else:
                t += 1
        max_h = max(t, max_h)

        t = 0
        for i in range(1, len(vBars)):
            if vBars[i-1] + 1 != vBars[i]:
                max_v = max(t, max_v)
                t = 0
            else:
                t += 1
        max_v = max(t, max_v)

        return min(max_h+2, max_v+2) ** 2