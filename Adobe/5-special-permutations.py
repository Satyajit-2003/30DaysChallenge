from functools import cache
from typing import List

# Use bitmasking to keep track of the elements used
# Use recursion to find all the permutations
# Use cache to store the results of the subproblems

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        end = (1 << n) - 1   # When all ones in the bitmask

        @cache
        def count(last, mask):
            if mask == end:
                return 1
            
            total = 0
            for i in range(n):
                if (mask & (1 << i) == 0) and ((nums[i] % nums[last] == 0) or (nums[last] % nums[i] == 0)):
                    total += count(i, mask | (1 << i))
            return total % MOD
        
        total = 0
        for i in range(n):
            total += count(i, (1 << i))
        return total % MOD