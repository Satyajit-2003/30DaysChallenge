from typing import List

# The equation for F(n) is: 
# F(n) = F(n-1) + total_sum_of_all_elements - n*A[n-1]
# This is because, all elements are shifted to the right by 1, except the last element which is shifted 0.

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i, j in enumerate(nums):
            res += (i*j)
        total_sum = sum(nums)
        curr_sum = res

        for i in range(n-1, -1, -1):
            curr_sum += total_sum
            curr_sum -= (n*nums[i])
            res = max(res, curr_sum)
        
        return res