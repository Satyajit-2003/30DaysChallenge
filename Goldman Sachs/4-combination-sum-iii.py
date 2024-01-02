from typing import List

# Use backtracking to find all combinations of k numbers that add up to a number n, 
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        def backtrack(k, i, li, su):
            if su == n and k == 0:
                self.res.append(li.copy())
                return
            if su > n or i == 10:
                return
            
            # Take element i
            backtrack(k-1, i+1, li+[i], su+i)
            # Don't take element  i
            backtrack(k, i+1, li, su)

        backtrack(k, 1, [], 0)

        return self.res
