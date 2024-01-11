from collections import deque
from typing import Optional

# Convert the binary tree to an undirected graph
# Do a layer by layer BFS, and return the time it takes to visit all nodes

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def toGraph(self, node, parent):
        if parent:
            self.graph[node.val] = [parent.val]
        if node.left:
            self.graph[node.val].append(node.left.val)
            self.toGraph(node.left, node)
        if node.right:
            self.graph[node.val].append(node.right.val)
            self.toGraph(node.right, node)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.graph = {}
        self.graph[root.val] = []
        self.toGraph(root, None)

        q = deque()
        visit = set()
        q.append(start)
        visit.add(start)
        time = 0

        while q:
            time += 1
            for _ in range(len(q)):
                node = q.popleft()
                for nei in self.graph[node]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)

        return time - 1