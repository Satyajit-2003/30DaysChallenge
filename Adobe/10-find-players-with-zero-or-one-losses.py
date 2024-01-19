from typing import List

# Use hash table to store the number of wins and losses for each player
# Iterate through the hash table and append the player to the result list

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {}
        for w, l in matches:
            if w not in win:
                win[w] = 0

            if l not in win:
                win[l] = 1
            else:
                win[l] += 1
        
        res = [[],[]]
        for pl in sorted(win.keys()):
            if win[pl] == 0:
                res[0].append(pl)
            elif win[pl] == 1:
                res[1].append(pl)
        
        return res