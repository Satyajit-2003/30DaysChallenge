from typing import List
from collections import deque

# Mark all water cells as 0 and add them to queue, make all land cells as -1
# Start BFS from water cells and keep track of distance from water cells
# Do a multi-source BFS from water cells

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        m = len(isWater)
        n = len(isWater[0])
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    q.append((i, j))
                else:
                    isWater[i][j] = -1
                    
        while q:
            x, y = q.popleft()
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and isWater[i][j] == -1:
                    isWater[i][j] = isWater[x][y] + 1
                    q.append((i, j))
        
        return isWater