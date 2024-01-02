from typing import List

# As the constraints are small, we can brute force it.

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        arr = [(num, i) for i, num in enumerate(nums)]

        for k, trim in queries:
            arr.sort(key=lambda x: (x[0][-trim:], x[1]))
            res.append(arr[k-1][1])

        return res