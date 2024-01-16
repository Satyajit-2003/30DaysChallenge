from typing import List

# Sort the words by length in descending order.
# Iterate through the words, and for each word, check if it's in the result string.
# If not, append it to the result string.
# Return the length of the result string.

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(reverse = True, key = lambda x: len(x))
        res = ''
        for word in words:
            if word+'#' not in res:
                res += word + '#'
        
        return len(res)