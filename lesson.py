# 112.Path Sum

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isLeaf(self, root: Optional[TreeNode]):
        if root:
            # if child exists, that's not leaf
            if root.left or root.right:
                return False
            return True

        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            if self.isLeaf(root) and targetSum - root.val == 0:
                return True

            if self.isLeaf(root) and targetSum - root.val != 0:
                return False

            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

        return False
