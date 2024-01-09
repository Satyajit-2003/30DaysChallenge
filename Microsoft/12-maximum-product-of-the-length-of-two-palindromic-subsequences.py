# Use bitmasking to generate all possible subsequences and check if they are palindromes
# Basically brute force, the palindromes are stored in a hash table
# Then brute force the hash table to find the maximum product

class Solution:
    def maxProduct(self, s: str) -> int:
        N = len(s)
        hash = {}
        for mask in range(1, 2**N): # Maximum 2*n possible subsequences
            st = ''
            for i in range(N):
                if mask & (1 << i):
                    st += s[i]
            if st == st[::-1]:
                hash[mask] = len(st)
        
        res = 0
        for m1 in hash:
            for m2 in hash:
                if m1 & m2 == 0:
                    res = max(res, hash[m1]*hash[m2])
        
        return res            
                