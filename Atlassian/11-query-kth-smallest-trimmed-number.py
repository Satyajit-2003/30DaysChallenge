from typing import List

# Keep track of the number and its index in the original array
# For each query, sort the array by the last k digits
# Append the index of the kth smallest number to the result

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        arr = [(num, i) for i, num in enumerate(nums)]

        for k, trim in queries:
            arr.sort(key=lambda x: (x[0][-trim:], x[1]))
            res.append(arr[k-1][1])

        return res