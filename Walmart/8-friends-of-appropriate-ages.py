from typing import List

# Find the frequency of each age
# For each age, find if it can send request to all other ages
# If yes, add the product of their frequencies to total
# If age is same, subtract the frequency from total

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def request(a, b):
            if b <= 0.5 * a + 7 or b > a:
                return False
            return True
        freq = {}
        total = 0
        for n in ages:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        for age1, cnt1 in freq.items():
            for age2, cnt2 in freq.items():
                if request(age1, age2):
                    total += (cnt1 * cnt2)
                    if age1 == age2:
                        total -= cnt1
        return total