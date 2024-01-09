from typing import List

# Take each subarray and check if the array is incremental or not after removing the subarray
# Brute force 

class Solution:
    def isincr(self, nums, start, end):
        prev = 0
        for i in range(len(nums)):
            if start <= i <= end:
                continue
            if nums[i] <= prev:
                return False
            prev = nums[i]
        return True

    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        res = 0
        for start in range(len(nums)):
            for end in range(start, len(nums)):
                if self.isincr(nums, start, end):
                    print(nums, start, end)
                    res += 1
        
        return res