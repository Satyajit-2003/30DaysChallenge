# Use a hash to store the frequency of each character.
# Sort the hash by the frequency in descending order.
# Iterate through the sorted hash and append the character to the result string the number of times equal to its frequency.

class Solution:
    def frequencySort(self, s: str) -> str:
        hash = {}
        for ch in s:
            if ch in hash:
                hash[ch] += 1
            else:
                hash[ch] = 1
        
        res = ''
        for key, freq in sorted(hash.items(), key = lambda x: x[1], reverse = True):
            res += (key * freq)
        
        return res