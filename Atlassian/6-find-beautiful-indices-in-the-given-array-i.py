from typing import List

# Find all indices of a and b in s.
# For each index of a, find if the index is beautiful by checking if there is an index of b within k distance.

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        arr1 = []
        arr2 = []

        for i in range(len(s) - len(a) + 1):
            if s[i:i+len(a)] == a:
                arr1.append(i)
        
        for j in range(len(s) - len(b) + 1):
            if s[j:j+len(b)] == b:
                arr2.append(j)

        ans = []
        for i in arr1:
            for j in arr2:
                if abs(i-j) <= k:
                    ans.append(i)
                    break
                    
        ans.sort()
        return ans