# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node, answer):
            answer =  answer*10 + node.val
            node.val = answer
            print(node.val, answer)
            if node.left and node.right:
                return helper(node.left, answer) + helper(node.right, answer)
            elif node.right:
                return helper(node.right, answer)
            elif node.left:
                return helper(node.left, answer)
            else:
                return answer
        return helper(root, 0)


            