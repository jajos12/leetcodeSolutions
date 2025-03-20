# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        diff = 0
        def solver(node, maxim, minim):
            nonlocal diff
            if not node:
                return
            diff = max(diff, abs(maxim-node.val), abs(minim-node.val))
            maxim = max(node.val, maxim)
            minim = min(node.val, minim)
            solver(node.left, maxim, minim)
            solver(node.right, maxim, minim)
        solver(root, root.val, root.val)
        return diff
