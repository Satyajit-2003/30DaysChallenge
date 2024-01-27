from typing import List

# Itterate over the string and add each 10 letter sequence to a set.
# If the sequence is already in the set, add it to the result set.

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        found = set()
        res = set()

        for i in range(len(s)-9):
            if s[i:i+10] in found:
                res.add(s[i:i+10])
            else:
                found.add(s[i:i+10])
        
        return list(res)