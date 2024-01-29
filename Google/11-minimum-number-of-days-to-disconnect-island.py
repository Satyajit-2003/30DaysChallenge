from collections import deque
from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count():
            ans = 0
            visited = set()

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        ans += 1

                        q = deque([[i, j]])
                        visited.add((i, j))

                        while q:
                            ni, nj = q.popleft()

                            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                                x, y = ni+dx, nj+dy

                                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == 1:
                                    q.append([x,y])
                                    visited.add((x,y))
            return ans
        
        m = len(grid)
        n = len(grid[0])
        if count() != 1:
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    grid[i][j] = 0
                    if count() != 1:
                        return 1
                    grid[i][j] = 1
        
        return 2