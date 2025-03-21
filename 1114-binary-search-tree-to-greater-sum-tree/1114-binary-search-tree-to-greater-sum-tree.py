# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = 0
        def solver(node):
            nonlocal temp
            if not node:
                return temp
            sth = solver(node.right)
            temp += node.val
            node.val += sth
            solver(node.left)
            return temp
        sum_ = solver(root)
        return root