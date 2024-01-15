from typing import List

# Make a decision at each index i to skip or not skip the current char
# If skipping, then we need to add 1 to the result
# If not skipping, then we have to check all the substrings starting from i
# and see if they are present in the dictionary

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        def helper(i):
            if i == len(s):
                return 0
            if i in cache:
                return cache[i]
            
            # Skipping the current char
            res = 1 + helper(i+1)
            # Not skipping 
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    res = min(res, helper(j+1))
            cache[i] = res
            return res
        
        words = set(dictionary)
        cache = {}
        return helper(0)