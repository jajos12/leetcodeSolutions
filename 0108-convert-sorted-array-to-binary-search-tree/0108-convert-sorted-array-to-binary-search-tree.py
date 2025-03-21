# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        def solver(left, right):
            if left > right:
                return None
            half = (left+right)//2
            node = TreeNode(nums[half])
            node.left = solver(left, half-1)
            node.right = solver(half+1, right)
            return node
        root = solver(0, n-1)
        return root

