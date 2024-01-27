import heapq
from typing import List

# Add the sumof values of each index to a max heap
# Pop the max value and add it's corresponding value to the player's score
# The player with the highest score wins

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        heap = []   # (value, index)
        for i in range(len(aliceValues)):
            heapq.heappush(heap, (-aliceValues[i] - bobValues[i], i))
        
        alice = bob = 0
        for i in range(len(aliceValues)):
            if i % 2 == 0:
                alice += aliceValues[heapq.heappop(heap)[1]]
            else:
                bob += bobValues[heapq.heappop(heap)[1]]
        if alice > bob:
            return 1
        if alice < bob:
            return -1
        return 0
