import heapq
from typing import List

# Create a bidirectional graph with weights
# Use Dijkstra's algorithm on each node
# For each node, count the number of nodes that are reachable within the distanceThreshold

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [{}  for _ in range(n)]

        for src, dst, w in edges:
            graph[src][dst] = w
            graph[dst][src] = w
        
        res = float('inf')
        res_city = -1

        for city in range(n):
            dist = [-1 for _ in range(n)]
            heap = [(0, city)]
            while heap:
                wei, node = heapq.heappop(heap)
                if dist[node] != -1:
                    continue
                dist[node] = wei

                for nei, w in graph[node].items():
                    if dist[nei] == -1:
                        heapq.heappush(heap, (wei + w, nei))
            req = sum(1 for i in dist if 0 < i <= distanceThreshold)
            
            if req < res:
                res = req
                res_city = city
            elif req == res:
                res_city = max(res_city, city)

        return res_city