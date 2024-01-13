from typing import List

# Create a 2D array of size len(nums1) + 1 and len(nums2) + 1
# If the elements are same, then add 1 to the previous diagonal element
# return the maximum element in the array

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums2) + 1)] for __ in range(len(nums1) + 1)]
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    print(i, j, len(dp) , len(dp[0]))
                    dp[i+1][j+1] = dp[i][j] + 1
                    res = max(res, dp[i+1][j+1])
        
        return res
    