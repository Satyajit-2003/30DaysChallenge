# Post order traverse the tree and return the distance of each leaf node to the root node.
# Then, for each pair of leaf nodes, check if the sum of their distances is less than or equal to the given distance.   


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def travserse(self, node):
        if not node:
            return []
        if not node.left and not node.right:
            return [1]
        left = self.travserse(node.left)
        right = self.travserse(node.right)

        for l in left:
            if l >= self.tar:
                continue
            for r in right:
                if l + r <= self.tar:
                    self.res += 1
        
        return [1+x for x in left+right]       
        
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root:
            return 0
        self.tar = distance
        self.res = 0
        self.travserse(root)

        return self.res