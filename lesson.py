# 94.Binary Tree Inorder Traversal
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.l = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            self.inorderTraversal(root.left)
            self.l.append(root.val)
            self.inorderTraversal(root.right)
        return self.l
