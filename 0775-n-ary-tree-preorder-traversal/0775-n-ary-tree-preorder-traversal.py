"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.output = []
    def helper(self, node):
        if not node:
            return
        self.output.append(node.val)

        for child in node.children:
            self.helper(child)

    def preorder(self, root: 'Node') -> List[int]:
            self.helper(root)
            return self.output