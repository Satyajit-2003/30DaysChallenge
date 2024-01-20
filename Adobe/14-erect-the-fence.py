from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def isMoreClock(a, b, c):
            # > 0 -> c is more clockwise wrt a
            # < 0 -> b is more clockwise wrt a
            # 0 -> a, b, c on same line
            return (c[0] - a[0]) * (b[1] - a[1]) - (b[0] - a[0]) * (c[1] - a[1])
        
        n = len(trees)
        if n < 4:
            return trees
        
        cur = 0
        for i, (x, y) in enumerate(trees):
            if x < trees[cur][0]:
                cur = i

        leftmost = cur
        ans = set()

        while True:
            cand = (cur + 2) % n

            for i in range(n):
                if isMoreClock(trees[cur], trees[cand], trees[i]) > 0:
                    cand = i
            
            for i in range(n):
                if isMoreClock(trees[cur], trees[cand], trees[i]) == 0:
                    ans.add(( trees[i][0], trees[i][1] ))
                    print(i)
            print(cand)
            if cand == leftmost:
                break
            cur = cand
        
        return ans

print(Solution().outerTrees([[0,5],[10,0],[10,10],[0,10],[0,0]]))