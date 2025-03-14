# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solver(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            return left.val == right.val and solver(left.right, right.left) and solver(left.left, right.right)
        return solver(root, root)   