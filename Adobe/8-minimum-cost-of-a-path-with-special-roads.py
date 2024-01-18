from typing import List


class Solution:
    def neighbors(self, nodes, specialRoads) : 
        nbrs = {}
        for road in specialRoads :
            startX, startY, endX, endY, dist = road
            if (startX, startY) not in nbrs : 
                nbrs[(startX, startY)] = []
            nbrs[(startX, startY)].append(((endX, endY), dist))

        for i in range(len(nodes)) : 
            if nodes[i] not in nbrs : 
                nbrs[nodes[i]] = []
            for j in range(len(nodes)) : 
                if i != j : 
                    dist = abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1])
                    nbrs[nodes[i]].append((nodes[j], dist)) 

        return nbrs 

    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        nodes = [tuple(start), tuple(target)]
        for road in specialRoads :
            startX, startY, endX, endY, dist = road
            nodes.append((startX, startY))
            nodes.append((endX, endY))

        neighbors = self.neighbors(nodes, specialRoads)

        visited, distance, infinity = {}, {}, float('inf')
        for node in nodes : 
            visited[node], distance[node] = False, infinity

        distance[tuple(start)] = 0
        for _ in range(len(nodes)) : 
            if False in visited.values() :
                min_distance = min([
                    distance[node] for node in nodes if not visited[node]
                ])
            else :
                break 

            next_node_list = [
                node for node in nodes if not visited[node]
                and distance[node] == min_distance
            ]

            next_node = min(next_node_list)
            visited[next_node] = True 

            if next_node in neighbors :
                for nbr in neighbors[next_node] :
                    if not visited[nbr[0]] :
                        if min_distance + nbr[1] < distance[nbr[0]] : 
                            distance[nbr[0]] = min_distance + nbr[1]

        
        return distance[tuple(target)] if distance[tuple(target)] != infinity else -1
        