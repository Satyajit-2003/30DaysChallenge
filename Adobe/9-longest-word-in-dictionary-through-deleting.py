from typing import List

# Check if each word in the dictionary is a subsequence of the string s
# If it is, check if it is longer and lexicographically smaller than the current longest word
# If it is, update the longest word

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def issubseq(word, s):
            i = j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            return True if i == len(word) else False
        
        res = ''
        for word in dictionary:
            if len(word) < len(res):
                continue
            if issubseq(word, s): 
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res):
                    res = min(res, word)
        
        return res