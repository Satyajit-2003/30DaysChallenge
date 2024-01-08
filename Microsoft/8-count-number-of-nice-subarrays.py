from typing import List

# Imagine odd numbers are 1 and even numbers are 0.
# Use a prefix sum to find the number of subarrays with k odd numbers.
# Use a hash to store the number of subarrays with a given prefix sum.
# Search for the number of subarrays with prefix curr_sum - k.

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hash = {}
        res = 0
        prefix_sum = 0

        for n in nums:
            if n % 2:
                prefix_sum += 1
            
            if prefix_sum == k:
                res += 1
            if prefix_sum not in hash:
                hash[prefix_sum] = 1
            else:
                hash[prefix_sum] += 1

            req = prefix_sum - k
            if req in hash:
                res += hash[req]
                        
        return res
        

