# 100.Same Tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []

        def inorder(node: TreeNode, l: list):
            if not node:
                l.append(None)
                return

            inorder(node.left, l)
            l.append(node.val)
            inorder(node.right, l)

        inorder(p, l1)
        inorder(q, l2)

        if l1 == l2:
            return True

        return False
