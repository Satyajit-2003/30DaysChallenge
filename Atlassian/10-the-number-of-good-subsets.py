from typing import List
from collections import Counter

# Use bitmask to represent the prime factors of a number
# Find the count of each number
# Use dfs to find the number of good subsets

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2,3,5,7,11,13,17,19,23,29]
        def get_mask(n):
            mask = 0
            for i in range(len(primes)):
                if n % primes[i] == 0:
                    n /= primes[i]
                    mask |= (1 << i)
                if n % primes[i] == 0:
                    return -1
            return mask
        
        count = Counter(nums)
        arr = list(count.keys())
        n = len(arr)
        mod = 1000000007

        def dfs(i, mask):
            if i == n:
                return 1
            
            # Skip i
            res = dfs(i+1, mask)

            # Take i
            curr_mask = get_mask(arr[i])
            if curr_mask != -1 and arr[i] != 1 and curr_mask & mask == 0:
                res += (dfs(i+1, mask | curr_mask) * count[arr[i]]) % mod
            
            return res
        
        return (dfs(0, 0) * pow(2, count[1], mod)) % mod

        
