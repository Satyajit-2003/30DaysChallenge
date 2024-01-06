# Maintain an array of all the players.
# Find the nxt player to be removed by adding k to the current player's index and taking the modulo of the length of the array.

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i+1 for i in range(n)]
        loser = 0
        while len(arr) > 1:
            loser = (loser+k-1) % len(arr)
            arr.pop(loser)
        return arr[0]