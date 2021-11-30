from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_leaf(self, root: Optional[TreeNode]) -> bool:
        if root:
            if root.left or root.right:
                return False
            return True

        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            if self.is_leaf(root) and targetSum - root.val == 0:
                return True

            if self.is_leaf(root) and targetSum - root.val != 0:
                return False

            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
