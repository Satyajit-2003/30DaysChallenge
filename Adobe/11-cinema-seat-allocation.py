from collections import defaultdict
from typing import List

# Keep track of the reserved seats in a hash table
# Iterate through the hash table and count the number of families
# Add a number to the set if a set of seats is reserved
# Take the initial result as 2 * n
# Subtract 1 or 2 from the result if a set of seats is reserved

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        hash = defaultdict(set)

        for i, j in reservedSeats:
            if j in [2,3,4,5]:
                hash[i].add(0)
            if j in [4,5,6,7]:
                hash[i].add(1)
            if j in [6,7,8,9]:
                hash[i].add(2)
        
        res = 2 * n
        for i in hash:
            if len(hash[i]) == 3:
                res -= 2
            else:
                res -= 1

        return res