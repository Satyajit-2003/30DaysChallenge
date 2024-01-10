from typing import List

# Initialize the graph by taking the minimum cost from each character to each other character [26*26] matrix
# Use Floyd-Warshall algorithm to find shortest path between all pairs of nodes
# Then, for each character in source, find the shortest path to the corresponding character in target

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[float('inf') for _ in range(26)] for __ in range(26)]
        for i in range(len(changed)):
            src = ord(original[i]) - 97
            dst = ord(changed[i]) - 97
            graph[src][dst] = min(graph[src][dst], cost[i])
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        cost = 0

        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            src = ord(source[i]) - 97
            dst = ord(target[i]) - 97
            if graph[src][dst] == float('inf'):
                return -1
            cost += graph[src][dst]
        
        return cost