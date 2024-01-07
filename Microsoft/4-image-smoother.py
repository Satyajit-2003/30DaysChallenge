from typing import List

# Use a list of tuples to iterate through the 9 cells around each cell
# If the cell is valid, add the value to the sum and increment the count
# Add the average to the new matrix


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = []

        for i in range(len(img)):
            res.append([])
            for j in range(len(img[0])):
                add = cnt = 0
                for dx, dy in [(0,0), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < len(img) and 0 <= y < len(img[0]):
                        add += img[x][y]
                        cnt += 1
                res[-1].append(add//cnt)

        return res