from typing import List


# Sort and find median
# Calculate the difference between each number and the median

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) % 2 == 0:
            median = (nums[len(nums)//2] + nums[len(nums)//2 - 1]) // 2
        else:
            median = nums[len(nums)//2]
            
        res = 0
        for n in nums:
            res += abs(median - n)
        
        return res