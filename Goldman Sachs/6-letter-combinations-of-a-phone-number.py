from typing import List

# Use backtracking

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.res = []
        self.chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(i, ans):
            if i == len(digits):
                self.res.append(ans)
                return
            for ch in self.chars[digits[i]]:
                backtrack(i+1, ans+ch)
        
        backtrack(0, '')
        return self.res