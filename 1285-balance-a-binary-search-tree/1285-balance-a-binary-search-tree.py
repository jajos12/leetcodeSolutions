# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        def build(left, right):
            if left > right:
                return None
            half = (left+right)//2
            node = TreeNode(arr[half])
            node.left = build(left, half-1)
            node.right = build(half+1, right)
            return node
        
        inorder(root)
        return build(0, len(arr)-1)