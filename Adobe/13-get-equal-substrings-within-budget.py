# First find the difference between the characters of the two strings and store it in an array.
# Then use sliding window to find the maximum length of the substring with cost less than or equal to maxCost.

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr = []
        for i in range(len(s)):
            arr.append(abs ( ord(s[i]) - ord(t[i]) ))
        l = 0
        max_len = 0
        cost = 0
        i = j = 0
        while j < len(arr):
            cost += arr[j] 
            while cost > maxCost:
                cost -= arr[i]
                i += 1
            max_len = max(max_len, j-i+1)
            j += 1
        return max_len
        