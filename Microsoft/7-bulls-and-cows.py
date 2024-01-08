# Count the bulls first by comparing the same index of secret and guess.
# Then count the cows by using a hash table to store the number of each digit in secret and guess.
# If the digit is in secret, increment the value by 1. If the digit is in guess, decrement the value by 1.
# The number of cows is the number of digits in secret and guess that are not bulls.

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        hash = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] not in hash:
                    hash[secret[i]] = -1
                else:
                    hash[secret[i]] -= 1
                
                if guess[i] not in hash:
                    hash[guess[i]] = 1
                else:
                    hash[guess[i]] += 1
                    
        not_any = 0
        for n in hash.values():
            not_any += abs(n)
        not_any //= 2
        cows = len(secret) - not_any- bulls

        return str(bulls)+'A'+str(cows)+'B'