# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        self.avg = 0
        def solver(node, temp, cnt):
            if not node:
                return (0, 0)
            left = solver(node.left, temp, cnt+1)
            right = solver(node.right, temp+node.val, cnt+1)
            cnt = left[0] + right[0] + 1
            temp = left[1] + right[1] + node.val
            if cnt > 0 and node.val == temp//cnt:
                self.count += 1
            return (cnt, temp)
        solver(root, 0, 0)
        return self.count