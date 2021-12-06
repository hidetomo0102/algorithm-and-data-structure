# 145.Binary Tree PostOrder Traversal
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    ans = []

    def _inorder(root: TreeNode, ans: list):
        if root:
            _inorder(root.right, ans)
            _inorder(root.left, ans)
            ans.append(root.val)

    _inorder(root, ans)
    return ans
