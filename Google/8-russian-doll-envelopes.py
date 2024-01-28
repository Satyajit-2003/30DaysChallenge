from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def binary(arr, start, end, val):
            while start < end:
                mid = (start + end)//2

                if arr[mid] == val:
                    return mid
                elif arr[mid] < val:
                    start = mid + 1
                else:
                    end = mid
            return start

        envelopes.sort(key = lambda x: (x[0], -x[1]))

        dp = [0 for i in range(len(envelopes))]
        res = 0

        for i in range(len(envelopes)):
            idx = binary(dp, 0, res, envelopes[i][1])

            dp[idx] = envelopes[i][1]
            if idx == res:
                res += 1
        
        return res