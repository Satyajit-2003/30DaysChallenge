from typing import List

# Go through the board and check for 'X'
# If 'X' is found, check if its prev row and col are 'X'
# If not, then its a new ship
# This is because there are no adjacent ships

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ships = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                # As there are no adjacent ships, so a new ship must have its prev row and cols not be part of a ship
                if (board[i][j] == 'X' and 
                (i == 0 or board[i-1][j] != 'X') and 
                (j == 0 or board[i][j-1] != 'X')):
                    ships += 1
        
        return ships
