from typing import List
from sortedcontainers import SortedList

# Go through the buildings and add the start and end points of each building to a list of events.
# Sort the events by x coordinate.
# Go through the events having same x cordinate at once. For each event:
# If the event is a start point, add the height to a set of active heights.
# If the event is an end point, remove the height from the set.
# If the current maximum height in the set of active heights is different from the previous height in the skyline, 
# add the current event's x coordinate and the current maximum height to the skyline.

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        ans = []
        for s, e, h in buildings:
            events.append((s, h, 0))
            events.append((e, h, 1))
        events.sort()

        i = 0
        heights = SortedList([0])

        while i < len(events):
            curr_x = events[i][0]

            while i < len(events) and events[i][0] == curr_x:
                x, h, t = events[i]

                if t == 0:
                    heights.add(h)
                else:
                    heights.remove(h)
                i += 1
            
            if not ans or ans[-1][1] != heights[-1]:
                ans.append((curr_x, heights[-1]))
        
        return ans