# 101.Symmetric Tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            return self._is_symmetric(root.left, root.right)
        else:
            return True

    def _is_symmetric(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        elif not left or not right:
            return False
        else:
            return self._is_symmetric(left.right, right.left) and right.val == left.val and self._is_symmetric(
                left.left, right.right)
