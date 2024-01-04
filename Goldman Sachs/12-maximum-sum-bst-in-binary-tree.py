from typing import Optional

# Use a recursive function to calculate the sum of a subtree
# If the subtree is a BST, then update the max sum
# Return the sum, minL and maxR value of the subtree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def calc(self, node):
        if not node:
            return [0, float('-inf'), float('inf')]
        if not (node.left or node.right):
            self.ans = max(node.val, self.ans)
            return [node.val, node.val, node.val]

        sum1, minL, _1 = self.calc(node.left)
        sum2, _2, maxR = self.calc(node.right)

        if minL < node.val < maxR:
            ans = node.val + sum1 + sum2
            self.ans = max(self.ans, ans)
            return [ans, max(node.val, _2), min(node.val, _1)]
        return [max(sum1, sum2), float('inf'), float('-inf')]

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.calc(root)
        return self.ans