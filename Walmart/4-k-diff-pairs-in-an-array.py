from typing import List

# Take two sets, visit and set
# Look for num-k and num+k in visit set
# If found, add to result set in ascending order
# Add num to visit set
# Return length of result set

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = set()
        visit = set()
        for num in nums:
            if num-k in visit:
                res.add((num-k, num))
            if num+k in visit:
                res.add((num, num+k))
            visit.add(num)

        return len(res)