import heapq
from typing import List

# Mathematically, the max product will be achieved by incrementing the smallest values
# Put all vales in a min heap
# Pop the min value and increment it by 1, k times
# Multiply all values in the heap together and return the result

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 1000000007
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heappush(nums, heapq.heappop(nums)+1)
        
        res = 1
        for n in nums:
            res = (res * n) % MOD
        
        return res