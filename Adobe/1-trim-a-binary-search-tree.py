# Definition for a binary tree node.
from typing import Optional

# If root is smaller than low, then all nodes in the left subtree are smaller than low, so we can just do operation on the right subtree.
# If root is larger than high, then all nodes in the right subtree are larger than high, so we can just do operation on the left subtree.
# If root is in the range, then we recursively trim its left and right subtree.
# Return the root.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root