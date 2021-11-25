# 104.Maximum Depth of Binary Tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode], res=0) -> int:
        if not root:
            return res

        return max(self.maxDepth(root.left, res + 1), self.maxDepth(root.right, res + 1))
