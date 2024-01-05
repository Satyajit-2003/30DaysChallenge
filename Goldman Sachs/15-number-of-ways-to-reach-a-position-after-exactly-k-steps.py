from functools import cache

# Use cache to memoize the results of the recursive calls
# Basically brute force, but with memoization

class Solution:
    @cache
    def go(self, pos, k):
        if pos == self.end and k == 0:
            return 1
        if k == 0:
            return 0
        return self.go(pos+1, k-1) + self.go(pos-1, k-1)

    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        self.end = endPos       
        return self.go(startPos, k) % ((10**9) + 7)