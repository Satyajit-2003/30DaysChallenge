from typing import List

# First sort the envelopes by width, then by height in descending order.
# Then the problem becomes finding the longest increasing subsequence of the heights.

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        n = len(envelopes)
        longest_increasing_subsequence = [float('inf')] * (n + 1)
        longest_increasing_subsequence[0] = -float('inf')

        longest = 0
        for (_, h) in envelopes:
            index = self._get_gte(longest_increasing_subsequence, h)
            longest_increasing_subsequence[index] = h
            longest = max(longest, index)
        
        return longest
    
    def _get_gte(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] >= target:
            return start
        return end
        