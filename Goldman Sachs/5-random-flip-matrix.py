import random
from typing import List

# No need to initialize the matrix
# Just need to keep track of the flipped cells

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.flipped = set()

    def flip(self) -> List[int]:
        while 1:
            x = random.randint(0, self.m-1)
            y = random.randint(0, self.n-1)
            if (x, y)in self.flipped:
                continue
            break
        self.flipped.add((x, y))
        return [x, y]

    def reset(self) -> None:
        self.flipped.clear()        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()