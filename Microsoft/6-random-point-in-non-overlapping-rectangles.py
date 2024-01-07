from typing import List
import random



class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

    def pick(self) -> List[int]:
        total_area = 0
        chosen_p = [0,0]
        for rect in self.rects:
            h = abs(rect[3]-rect[1]+1)
            w = abs(rect[2]-rect[0]+1)
            area = h*w
            total_area += area
            if random.random()<area/total_area:
                p_y = random.randint(rect[1], rect[3])
                p_x = random.randint(rect[0], rect[2])
                chosen_p = [p_x, p_y]
        return chosen_p


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()