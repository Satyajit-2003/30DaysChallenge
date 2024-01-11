from typing import List
import heapq

# Convert the list to a max heap, along with the index
# Pop the heap k times, and sort the result by index

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = [(-j, i) for i, j in enumerate(nums)]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap))
        print(res)
        res.sort(key = lambda x: x[1])

        return [-i[0] for i in res]