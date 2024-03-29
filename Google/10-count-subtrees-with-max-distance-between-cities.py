from collections import defaultdict, deque
from typing import List


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        def getDist(mask):
            if mask & (mask-1) == 0:
                return 0

            ans = 0
            for i in range(n):
                if mask & (1<<i) == 0:
                    continue
                q = deque([i])
                temp = mask
                temp ^= (1<<i)
                d = 0

                while q:
                    for _ in range(len(q)):
                        node = q.popleft()

                        for nei in graph[node]:
                            if temp & (1 << nei):
                                q.append(nei)
                                temp ^= (1<<nei)
                    d += 1

                if temp:
                    return 0
                
                ans = max(ans, d)
            
            return ans-1
        
        res = [0] * (n-1)

        for mask in range(1<<n):
            d = getDist(mask)
            print(d)
            if d:
                res[d-1] += 1
        
        return res