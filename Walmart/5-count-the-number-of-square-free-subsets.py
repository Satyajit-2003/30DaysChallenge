from typing import List
import math
from collections import defaultdict

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7 

        def sfs_for_set(_set):
            if not _set:
                return 1
            current_set = []
            for num in _set[1:]:
                if math.gcd(num, _set[0]) == 1:
                    current_set.append(num)
            return (
                sfs_for_set(_set[1:]) + counter_map[_set[0]] * sfs_for_set(current_set)
            ) % MOD

        candidates = set(
            [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]
        )
        counter_map = defaultdict(int)
        for num in nums:
            if num in candidates:
                counter_map[num] += 1
        return (sfs_for_set(list(counter_map)) * 2 ** nums.count(1) - 1) % MOD
