from typing import List

# Use count sort
# Traverse the freq array from the end
# Fill odd indices with largest numbers 1, 3, 5, ...
# Fill even indices next, continuing to traverse from end 0, 2, 4, ...


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Using count sort
        freq = [0 for _ in range(5001)]
        for num in nums:
            freq[num] += 1
        
        key = 5000
        for i in range(1, len(nums), 2):
            while freq[key] == 0:
                key -= 1
            nums[i] = key
            freq[key] -= 1
        
        for i in range(0, len(nums), 2):
            while freq[key] == 0:
                key -= 1
            nums[i] = key
            freq[key] -= 1
        
        