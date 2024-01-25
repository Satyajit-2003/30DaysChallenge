from collections import defaultdict
from typing import List

# Use a sliding window to keep track of the frequency of each element
# If the frequency of an element exceeds k, move the left pointer until the frequency of the element is less than or equal to k
# Keep track of the maximum length of the subarray

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = r = 0
        res = 0
        hash = defaultdict(int)

        while r < len(nums):
            hash[nums[r]] += 1
            while hash[nums[r]] > k:
                hash[nums[l]] -= 1
                l += 1
            r += 1
            res = max(res, r-l)
        
        return res