from typing import List

# Check all subarrays of size k for divisibility by p
# Add it in a set to get distinct subarrays

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        res = set()
        for i in range(len(nums)):
            c = 0
            for j in range(i, len(nums)):
                if nums[j] % p == 0:
                    c += 1
                if c > k:
                    break
                
                res.add(tuple(nums[i:j+1]))
        
        return len(res)