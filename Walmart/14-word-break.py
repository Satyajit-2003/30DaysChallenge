from typing import List

# Use a boolean DP array of length n+1
# dp[i] = True if s[i:] can be segmented into words from the dictionary
# dp[i] = dp[i+n] if s[i:i+n] is a word in the dictionary
# dp[i] = False if no such word exists
# return dp[0]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[-1] = True

        for i in range(len(s), -1, -1):
            for word in wordDict:
                n = len(word)
                if i+n <= len(s) and s[i:i+n] == word:
                    dp[i] = dp[i+n]
                if dp[i]:
                    break
        
        return dp[0]
