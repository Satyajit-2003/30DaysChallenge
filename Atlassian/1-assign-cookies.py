from typing import List

# Use a greedy approach
# Sort both lists
# Iterate through the cookies and the children
# If the cookie is large enough, give it to the child and move on to the next child
# If the cookie is too small, move on to the next cookie
# Return the number of children that got a cookie

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        k = 0
        for cookie in s:
            if cookie >= g[k]:
                k += 1
            if k == len(g):
                return k
        
        return k