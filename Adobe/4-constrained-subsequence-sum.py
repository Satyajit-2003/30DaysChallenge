from typing import List
import heapq

# Maintain a max heap with element as (max_sum, index)
# We have to check the max in the last k indices of the array
# So, we pop elements from the heap which are not in the range of k
# Then, we calculate the max sum for the current index
# And push it into the heap
# Side by side we keep track of the max sum for the whole array

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # Simulating a max heap, by usinh -ve values
        heap = [(-nums[0], 0)] # (max_sum, index)
        res = nums[0]

        for i in range(1, len(nums)):
            while i - heap[0][1] > k:
                heapq.heappop(heap)

            curr_max = max(nums[i], nums[i] + (-heap[0][0]))
            res = max(res, curr_max)
            heapq.heappush(heap, (-curr_max, i))
        
        return res
            