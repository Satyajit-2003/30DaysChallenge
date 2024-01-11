from typing import List

# Sort the array
# Take two arrays, dp and next
# Use LIS approach, but check if nums[j] % nums[i] == 0
# dp[i] = length of largest divisible subset ending at nums[i]
# next[i] = index of next element in the largest divisible subset ending at nums[i]
# Take a note of start and max_len after each iteration
# Find the largest divisible subset using start and next array

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [-1 for i in range(len(nums))]
        next = [-1 for i in range(len(nums))]
        start = max_len = 0

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    next[i] = j
            if dp[i] > max_len:
                start = i
                max_len = dp[i]

        res = []
        while start != -1:
            res.append(nums[start])
            start = next[start]
        
        return res
